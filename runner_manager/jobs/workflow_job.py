from __future__ import annotations

from githubkit.webhooks.models import (
    WorkflowJobCompleted,
    WorkflowJobInProgress,
    WorkflowJobQueued,
)

from runner_manager.clients.github import GitHub
from runner_manager.dependencies import get_github
from runner_manager.logging import log
from runner_manager.models.runner import Runner
from runner_manager.models.runner_group import RunnerGroup


def completed(webhook: WorkflowJobCompleted) -> int:
    log.info(f"Starting {webhook.action} workflow_job event")
    runner_group: RunnerGroup | None = RunnerGroup.find_from_webhook(webhook)
    runner: Runner = Runner.find_from_webhook(webhook)
    if not runner_group or not runner:
        log.warning(f"Runner {webhook.workflow_job.runner_name} not found")
        return 0
    log.info(f"Deleting runner {runner.name} in group {runner_group.name}")
    delete = runner_group.delete_runner(runner)
    if runner_group.need_new_runner:
        log.info(f"Runner group {runner_group.name} needs a new runner")
        github: GitHub = get_github()
        runner_group.create_runner(github)
    return delete


def in_progress(webhook: WorkflowJobInProgress) -> str | None:
    log.info(f"Starting {webhook.action} workflow_job event")
    name: str | None = webhook.workflow_job.runner_name
    runner_group: RunnerGroup | None = RunnerGroup.find_from_webhook(webhook)
    if not runner_group:
        log.info(f"Runner group for {name} not found")
        return None
    log.info(f"Updating runner {name} in group {runner_group.name}")
    runner: Runner = runner_group.update_runner(webhook=webhook)
    log.info(f"Runner {name} in group {runner_group.name} has been updated")
    return runner.pk


def queued(webhook: WorkflowJobQueued) -> str | None:
    log.info(f"Starting {webhook.action} workflow_job event")
    labels = webhook.workflow_job.labels
    log.info(f"Finding runner group with labels {labels}")
    runner_group: RunnerGroup = RunnerGroup.find_from_labels(
        webhook.workflow_job.labels
    )
    if not runner_group:
        log.warning(f"Runner group with labels {labels} not found")
        return None
    log.info(f"Found runner group {runner_group.name}")
    log.info(f"Creating registration token for runner {runner_group.name}")
    github: GitHub = get_github()
    log.info("Registration token created.")
    runner: Runner | None = runner_group.create_runner(github)
    return runner.pk if runner else None

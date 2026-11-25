# Code To Paper

## Goal

Convert any AI/ML/robotics repository into a paper story. Do not summarize files. Connect implementation artifacts to research claims along the ladder from code artifact to research abstraction, claim, needed evidence, and paper section.

## Abstraction Ladder

Use these mappings where relevant.

| Repository evidence | Paper abstraction |
| --- | --- |
| README, demo, examples, scripts | Task setting, user workflow, evaluation scope |
| Data pipeline, preprocessing, simulator, collector | Problem assumptions and deployment constraints |
| Model, policy, optimizer, sampler, controller | Intervention point |
| Objective, loss, rule, planner, search, memory, state | Mechanism |
| Profiling, error logs, failure cases, oracle labels | Bottleneck or observation |
| Config flags, thresholds, budgets, schedules, seeds | Ablation axes |
| Metrics, logs, checkpoints, output artifacts | Evidence for claims |

If the code only reveals an implementation detail, ask what assumption makes this detail necessary, what bottleneck it addresses, and what would fail without it.

## Repository Reading Guide

1. `README`, project page, scripts to see what problem the repository claims to solve.
2. Entrypoints to see what a user actually runs and which workflow changes.
3. Data and environment code to see what distribution, task, or deployment constraint defines the problem.
4. Core model, training, and inference modules to find where the proposed intervention enters the pipeline.
5. Objectives, controllers, memory or state, constraints, and decision rules to identify mechanisms that become method sections.
6. Configs, tests, evaluation scripts, and logs to identify ablation knobs, metrics, baselines, and reproducibility claims.

## General Story Archetypes

These examples help interpret a repository. Use the reasoning that fits the project rather than forcing an archetype.

### Efficiency Or Systems

Signs include profiling, caching, pruning, batching, scheduling, approximation, compiler or runtime changes, and memory reuse.

Story. A standard pipeline wastes compute, memory, or wall-clock time because it treats all instances, steps, or modules uniformly. The method identifies structure or redundancy and allocates computation selectively while preserving quality.

Evidence. Latency, throughput, FLOPs, memory, quality metric, overhead breakdown, and compatibility with larger settings.

### Robustness Or Data Quality

Signs include filtering, reweighting, curriculum, uncertainty, disagreement, clean or noisy labels, outliers, and adversarial or shifted data.

Story. Training or inference fails because the data or environment violates a common assumption. The method detects reliability, uncertainty, or difficulty and changes how samples, labels, states, or losses influence learning.

Evidence. Corrupted, noisy, or shifted benchmarks, hard subsets, sensitivity curves, and ablations on the reliability signal.

### Adaptation Or Control

Signs include policies, planners, closed-loop evaluation, online decisions, state-conditioned modules, and robot or environment feedback.

Story. A fixed policy or static design fails because the optimal behavior depends on context. The method uses observations, histories, or constraints to adapt decisions while maintaining stability and sample efficiency.

Evidence. Rollout success, recovery cases, generalization to new tasks, policy diagnostics, and real-time cost.

### Representation Or Architecture

Signs include a new encoder or decoder, attention pattern, graph, latent variable, tokenization, modular network, or cross-modal fusion.

Story. The existing representation hides or entangles a structure needed by the task. The method exposes that structure through an architectural or representational change, making learning, reasoning, or transfer easier.

Evidence. Main metrics, probing or visualization, module ablations, and transfer or scaling behavior.

### Optimization Or Objective

Signs include a new loss, regularizer, constraint, estimator, relaxation, search objective, or training schedule.

Story. The default objective optimizes the wrong proxy, has poor gradients, or ignores a constraint. The method reformulates the objective so the desired behavior is optimized more directly or stably.

Evidence. Convergence, stability, final performance, objective-component ablations, and sensitivity to hyperparameters.

### Evaluation Or Benchmark

Signs include a new dataset, metric, protocol, simulator, task suite, annotation pipeline, or diagnostic split.

Story. Current evaluation misses an important capability or failure mode. The contribution is a measurement frame plus evidence that existing methods behave differently under it.

Evidence. Benchmark construction, metric validity, baseline coverage, diagnostic findings, and reproducibility artifacts.

## Build The Initial Paper Frame

When asked to build from code, identify the core thesis, essential insight, actual mechanisms, and evidence needed to establish the claim. Propose an outline, figures, comparisons, and title candidates at the level of detail useful for the request.

Connect the implementation to the research question before listing components. The number of modules, figures, titles, or narrative stages should follow the project. Use [Style Transfer](style-transfer.md) to develop the argument and [Section Playbooks](section-frames.md) to draft sections.

## Evidence And Mechanism Accuracy

Check inputs, conditioning, representations, objectives, and operation order against the selected code and configuration. A smoother sentence must not change what the method actually does.

Treat code as evidence for implementation, not as proof of empirical gains or novelty. Support research claims with the relevant experiments or analysis, and attach citations to statements those sources actually support. Keep proposed evidence distinct from completed results.

Describe the insight and intervention rather than files, classes, head counts, or hidden-state lists. Promote an implementation choice to a contribution only when its research significance is explained and supported.

Report overhead, assumptions, and failure cases when they affect interpretation. Keep the explanation specific to the claim rather than appending stock reviewer-risk commentary.

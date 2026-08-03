# AI-assisted cloud engineering learning roadmap

## Purpose

This roadmap is the durable programme plan for becoming comfortable leading
AI-assisted engineering work as a cloud architect, cloud engineer, or DevOps
engineer. Codex may help inspect, plan, implement, test, review, and document,
but the learner remains responsible for requirements, architecture, security,
cost, correctness, and approval of changes.

The programme contains one foundation phase and seven projects. Durations are
guides rather than deadlines; progress depends on demonstrating the working
habits and completion gates, not merely producing an application.

## Programme outcomes

Across the programme, practise how to:

- turn vague requirements into bounded tasks and acceptance criteria;
- maintain context across fresh Codex sessions;
- review AI-generated changes instead of accepting them blindly;
- use branches, small commits, pull requests, tags, and releases;
- test and debug software, infrastructure, and delivery pipelines;
- use infrastructure as code without exposing secrets or state;
- analyse failures before modifying code;
- document architecture, decisions, operations, and lessons; and
- gradually coordinate larger components and independent workstreams.

## Sequence at a glance

| Stage | Project | Main focus | Approximate duration |
| --- | --- | --- | --- |
| Phase 0 | AI-assisted engineering foundations | Context, Git, review, safety | 2–3 sessions |
| Project 1 | Cloud Configuration Validator | Python CLI, tests, small branches | 1–2 weeks |
| Project 2 | Terraform Module and Policy Checks | IaC review and safe validation | 1–2 weeks |
| Project 3 | Containerised Service with CI/CD | Multi-file delivery and pipelines | 2 weeks |
| Project 4 | Cloud Operations and Cost Analysis Tool | Ambiguous requirements and reporting | 2 weeks |
| Project 5 | Kubernetes Deployment and GitOps Workflow | Deployment diagnosis and rollback | 2–3 weeks |
| Project 6 | Secure Cloud Platform Blueprint | Architecture across modules | 3 weeks |
| Project 7 | Self-Service Cloud Environment Platform | Capstone engineering leadership | 4–6 weeks |

Remote hosting, real cloud access, and paid services are not prerequisites.
Any exercise that needs GitHub or a cloud account begins only after the learner
explicitly chooses and verifies that setup. Prefer local fixtures, validation,
and simulations until then.

---

## Phase 0 — AI-assisted engineering foundations

### Goal

Create a reusable repository and a safe working method that survives terminal
and Codex restarts.

### Skills and deliverables

- Git installation, local author metadata, status, diff, staging, and history
- Focused commits and conventional commit messages
- `README.md`, `AGENTS.md`, architecture documentation, an ADR, a current
  project journal, changelog, ignore rules, and a pull request template
- A structural context check and a manual fresh-session resume exercise
- Clear separation between local Git, remote hosting, and authentication

### Completion gate

- A fresh Codex session reconstructs purpose, rules, status, and next action
  from repository evidence.
- The learner reviews the working tree and commit history.
- No remote, credential, or cloud dependency was assumed.

---

## Project 1 — Cloud Configuration Validator

- **Complexity:** Beginner
- **Primary technology:** Python and YAML
- **Cloud dependency:** None; local files only

### Goal

Build a command-line tool that validates fictional cloud workload definitions.
A workload may describe its application, environment, region, owner, network,
security settings, and governance tags.

### Initial validation rules

- Required fields must exist.
- A production workload must not allow unrestricted public access.
- Encryption must be enabled.
- Required tags such as cost centre and data classification must exist.
- The selected region must belong to an approved list.

### Learning focus

- Turn requirements into GitHub-style issues and acceptance criteria.
- Establish a maintainable Python project structure.
- Add unit tests, input validation, command-line help, and useful errors.
- Explain generated code and reject unnecessary abstractions.
- Recover from a deliberately introduced bug.

### Git and Codex exercises

- Implement validation concerns on focused branches such as
  `feature/required-fields`, `feature/security-rules`,
  `feature/tag-validation`, and `feature/json-output`.
- Ask Codex for analysis and a plan before implementation.
- Deliberately request an overly broad proposal, identify its scope creep, and
  narrow it before accepting changes.
- Review every staged diff before committing.

### Completion gate

- At least ten automated tests pass.
- Command-line help and errors are clear.
- CI runs tests on pull requests when a remote platform is configured; otherwise
  the workflow is created and inspected without assuming remote execution.
- Release `v0.1.0` is documented and tagged.
- Another engineer can use the tool from the README.

---

## Project 2 — Terraform Module and Policy Checks

- **Complexity:** Beginner–intermediate
- **Primary technology:** Terraform or OpenTofu and CI validation

### Goal

Build one reusable network module: either an AWS VPC or an Azure virtual
network. Choose one provider before implementation instead of supporting both.

### Scope

- Configurable address space
- Public and private subnets
- Resource naming and mandatory tags
- Useful outputs and example usage
- Variable validation and policy/security checks

No production deployment is required. Begin with formatting, static checks,
validation, and a reviewed plan where safe and available.

### Learning focus

- Module boundaries, inputs, outputs, compatibility, and documentation
- Terraform formatting, validation, and plan analysis
- Security defaults, provider assumptions, cost implications, and policy checks
- Protection of state, secrets, and local provider data

### Git and Codex exercises

- Require an architecture proposal before implementation.
- Challenge unnecessary resources, hard-coded values, insecure defaults,
  provider assumptions, cost, and backward-compatibility risks.
- Record a meaningful ADR.
- Amend an incorrect commit, revert a change safely, and prepare release
  `v1.0.0`.

### Completion gate

- Formatting and validation pass.
- Examples and inputs are documented.
- Security and policy checks have evidence.
- No secret or state file is committed.
- A reviewer can explain the expected infrastructure change without applying it.

---

## Project 3 — Containerised Service with CI/CD

- **Complexity:** Intermediate
- **Primary technology:** Python API, Docker, and CI/CD

### Goal

Create a small internal service with `GET /health`, `GET /version`, and
`GET /config-summary` endpoints. It reads configuration from environment
variables, emits structured logs, runs in a container, and has automated tests.

### Learning focus

- Multi-file feature development and dependency management
- Container image construction and runtime configuration
- Linting, tests, builds, and container security scanning
- Semantic versioning, release notes, and failed-pipeline diagnosis

### Git and Codex exercises

- Separate planning, implementation, and validation.
- Give Codex one endpoint or delivery concern at a time.
- Diagnose a deliberately failed CI build before changing files.
- Prevent unrelated container or pipeline work from leaking into a feature
  branch.

### Completion gate

- Endpoint, configuration, and error-path tests pass.
- The image builds reproducibly and runs as documented.
- Pipeline stages and failure conditions are understandable.
- A versioned image artifact can be exported or published when explicitly
  configured.

---

## Project 4 — Cloud Operations and Cost Analysis Tool

- **Complexity:** Intermediate
- **Primary technology:** Python, local cloud-style datasets, and reporting

### Goal

Analyse mock cloud inventory and billing data to identify unused resources,
missing owners, expensive resources, missing production backups, policy
violations, and potential monthly savings.

Begin with local JSON fixtures. A later optional branch may use an actual cloud
API only with explicit read-only credentials and an agreed safety boundary.

### Learning focus

- Clarifying the vague request: "Build something that finds cloud waste."
- Domain modelling and larger test datasets
- CSV and JSON reports
- Plugin-like analysis rules and separation of collection from analysis
- Mocked external dependencies and safe credential handling
- Critical review of AI-generated business logic

### Decision exercise

Use Codex to uncover questions, but have the learner decide:

- what qualifies as waste;
- which evidence is required;
- which assumptions are acceptable;
- which rules must be configurable; and
- how confidence and potential savings should be reported.

### Completion gate

- Rules have explicit definitions and representative tests.
- Recommendations show supporting evidence and assumptions.
- Reports are stable, useful, and documented.
- Data collection can be replaced without rewriting analysis logic.

---

## Project 5 — Kubernetes Deployment and GitOps Workflow

- **Complexity:** Intermediate–advanced
- **Primary technology:** Kubernetes, Helm or Kustomize, and CI validation

### Goal

Deploy the service from Project 3 to a local Kubernetes environment using
versioned, reviewable configuration.

### Scope

- Application manifests and environment overlays
- Resource requests and limits
- Health probes, ConfigMaps, and secret references
- Network policy and horizontal scaling configuration
- Deployment validation and rollback instructions

### Learning focus

- Application and platform repository boundaries
- GitOps-style environment changes
- Safe manifest generation and deployment testing
- Evidence-led diagnosis and rollback

### Failure exercises

Introduce and diagnose problems such as an incorrect container port, failing
readiness probe, missing configuration, invalid resource limits, broken image
tag, and excessive permissions. Codex should rank likely causes and cite logs,
events, and manifests before suggesting a change.

### Completion gate

- Manifests render and validate locally.
- Health, resources, configuration, and access controls are reviewed.
- At least one failure is diagnosed from evidence before repair.
- A tested rollback procedure is documented.

---

## Project 6 — Secure Cloud Platform Blueprint

- **Complexity:** Advanced
- **Primary technology:** Terraform, policy as code, CI/CD, and architecture docs

### Goal

Create a simplified enterprise platform blueprint spanning networking,
identity, logging, security, workloads, policy, and dev/test/prod environments.

### Scope

- Environment separation and reusable modules
- Central logging and identity/access patterns
- Naming and tagging standards
- Policy checks and CI validation
- Threat model, cost considerations, and ADRs

### Learning focus

- Managing a larger repository with directory-specific `AGENTS.md` files
- Coordinating related workstreams and reviewing cross-module changes
- Detecting unintended architectural changes and managing technical debt
- Structured security and cost review
- Using Codex as a reviewer as well as an implementer

### Team simulation

Balance fictional stakeholder requests: mandatory encryption from Security,
faster environments from developers, cost attribution from Finance, central
logging from Operations, and consistency from Architecture. Do not let Codex
satisfy each request independently without evaluating the system trade-offs.

### Completion gate

- Architecture boundaries and environment differences are explicit.
- Cross-cutting security, operations, and cost requirements have evidence.
- Policies and CI checks protect important decisions.
- Technical debt and trade-offs are visible rather than hidden.

---

## Project 7 — Capstone: Self-Service Cloud Environment Platform

**Complexity:** Advanced

### Goal

Build a small internal developer platform that accepts a configuration file or
API request for a standard cloud environment, validates it, generates an
infrastructure plan, enforces policy, and produces an auditable result.

### Components

- Request schema and validator
- Command-line interface or API
- Terraform modules and plan generation
- CI/CD workflows and policy checks
- Automated tests
- Architecture and decision documentation
- Logging and observability
- Release workflow and operational runbook
- Security threat model and cost-control rules

### Real-work practices

Use an issue backlog, milestones, feature branches, pull requests, review
checklists, releases, ADRs, bug reports, refactoring tasks, a simulated
production incident, and a final retrospective. Isolate independent Codex work
with separate branches or worktrees only after the learner is comfortable
reviewing and integrating each stream.

### Completion gate

- A request has a traceable path from validation through policy and planning.
- Security, cost, failure handling, and operations are documented and tested.
- Repository history demonstrates disciplined delivery rather than one large
  generated solution.
- The learner leads a simulated incident and explains the final architecture,
  trade-offs, and lessons without relying on Codex to make the decisions.

---

## Workflow for every task

Every feature, bug, or refactoring task follows this sequence:

1. Understand the requirement.
2. Write acceptance criteria.
3. Inspect the repository and working tree.
4. Ask Codex for a bounded plan.
5. Challenge assumptions and remove scope creep.
6. Create an appropriately named feature branch.
7. Create a safe Git checkpoint.
8. Implement one small portion.
9. Run relevant tests and validation.
10. Review the complete diff manually.
11. Ask Codex for a second review when useful.
12. Correct identified problems.
13. Stage deliberately and commit the focused outcome.
14. Write a pull request description.
15. Merge only when acceptance criteria are satisfied.
16. Record lessons and the next resume point.
17. Update `AGENTS.md` when a recurring lesson becomes a working rule.

## Increasing Codex autonomy

| Stage | Codex role | Learner responsibility |
| --- | --- | --- |
| Foundation | Explain and inspect | Understand every command |
| Project 1 | Suggest small edits | Approve individual changes |
| Project 2 | Implement scoped tasks | Review infrastructure diffs |
| Project 3 | Run tests and fix focused failures | Validate behaviour and security |
| Project 4 | Propose designs and refactoring | Challenge assumptions |
| Project 5 | Diagnose multi-component failures | Select and approve the solution |
| Project 6 | Work across modules | Protect architecture boundaries |
| Project 7 | Handle isolated workstreams | Lead the overall engineering process |

Autonomy increases only when tests are reliable, work is isolated, repositories
are clean, and the learner can inspect and reverse changes.

## Programme rules

1. Never begin an AI task with uncommitted work you cannot afford to lose.
2. Ask for analysis before implementation when a change is not trivial.
3. Give Codex one clearly bounded task at a time.
4. Never approve a command you do not understand.
5. Never commit code you cannot explain.
6. Treat tests as evidence, not proof of correctness.
7. Review the complete Git diff, not only Codex's summary.
8. Do not expose credentials, state files, customer data, or secrets.
9. Record architectural decisions outside chat sessions.
10. Correct repository instructions when Codex repeats a mistake.
11. Use branches and worktrees for isolation instead of broad access.
12. The learner remains accountable for the result.

## Assessment after each project

Score each area from 1 to 5 and record evidence in the project journal:

| Area | Assessment question |
| --- | --- |
| Requirements | Were scope and acceptance criteria clear? |
| AI collaboration | Did Codex receive enough context without receiving judgment authority? |
| Engineering | Is the solution understandable, tested, and maintainable? |
| Version control | Is history clean, reversible, and logically organised? |
| Validation | Were security and correctness independently verified? |

Before progressing, the learner should be able to explain the repository after
a restart, resume from durable context, identify what Codex changed, recover
from an unsuccessful change, distinguish suggestions from approved decisions,
and describe what would be done differently in a professional environment.

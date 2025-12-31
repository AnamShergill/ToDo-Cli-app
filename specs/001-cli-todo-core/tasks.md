---

description: "Task list for CLI Todo Core functionality implementation"
---

# Tasks: CLI Todo Core Functionality

**Input**: Design documents from `/specs/001-cli-todo-core/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Unit and integration tests are included as required by the specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/
- [ ] T002 Initialize Python project with proper directory structure (src/models/, src/services/, src/cli/, src/lib/, tests/unit/, tests/integration/)
- [ ] T003 [P] Create initial file placeholders for all required modules

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 [P] Create Task model in src/models/task.py based on data-model.md
- [ ] T005 [P] Create TaskManager service in src/services/task_manager.py for business logic
- [ ] T006 Create utility functions in src/lib/utils.py for input validation and formatting
- [ ] T007 Set up in-memory storage structure in TaskManager
- [ ] T008 Configure error handling infrastructure in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with a unique ID and pending status

**Independent Test**: Can be fully tested by adding a new task and verifying it appears in the task list, delivering the core value of task tracking.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Unit test for Task creation in tests/unit/test_task.py
- [ ] T010 [P] [US1] Unit test for add_task functionality in tests/unit/test_task_manager.py
- [ ] T011 [P] [US1] Integration test for adding tasks via CLI in tests/integration/test_cli.py

### Implementation for User Story 1

- [ ] T012 [US1] Implement add_task method in src/services/task_manager.py
- [ ] T013 [US1] Implement unique ID generation in src/services/task_manager.py
- [ ] T014 [US1] Implement task storage in src/services/task_manager.py
- [ ] T015 [US1] Add CLI command for adding tasks in src/cli/main.py
- [ ] T016 [US1] Add validation for task descriptions in src/lib/utils.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all their tasks with ID, description, and status

**Independent Test**: Can be fully tested by adding tasks and then viewing them, delivering the core value of task visibility.

### Tests for User Story 2 ⚠️

- [ ] T017 [P] [US2] Unit test for view_tasks functionality in tests/unit/test_task_manager.py
- [ ] T018 [P] [US2] Integration test for viewing tasks via CLI in tests/integration/test_cli.py

### Implementation for User Story 2

- [ ] T019 [US2] Implement view_tasks method in src/services/task_manager.py
- [ ] T020 [US2] Implement formatted display of tasks in src/lib/utils.py
- [ ] T021 [US2] Add CLI command for viewing tasks in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P2)

**Goal**: Enable users to mark tasks as complete to track progress and focus on remaining tasks

**Independent Test**: Can be fully tested by marking a task as complete and verifying its status changes, delivering the value of progress tracking.

### Tests for User Story 3 ⚠️

- [ ] T022 [P] [US3] Unit test for mark_complete functionality in tests/unit/test_task_manager.py
- [ ] T023 [P] [US3] Integration test for marking tasks complete via CLI in tests/integration/test_cli.py

### Implementation for User Story 3

- [ ] T024 [US3] Implement mark_complete method in src/services/task_manager.py
- [ ] T025 [US3] Update Task model to support status changes in src/models/task.py
- [ ] T026 [US3] Add CLI command for marking tasks complete in src/cli/main.py

**Checkpoint**: All user stories US1, US2, and US3 should now be independently functional

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Enable users to update task details to keep information accurate and up-to-date

**Independent Test**: Can be fully tested by updating a task and verifying the changes persist, delivering the value of task maintainability.

### Tests for User Story 4 ⚠️

- [ ] T027 [P] [US4] Unit test for update_task functionality in tests/unit/test_task_manager.py
- [ ] T028 [P] [US4] Integration test for updating tasks via CLI in tests/integration/test_cli.py

### Implementation for User Story 4

- [ ] T029 [US4] Implement update_task method in src/services/task_manager.py
- [ ] T030 [US4] Add CLI command for updating tasks in src/cli/main.py
- [ ] T031 [US4] Add validation for updated task descriptions in src/lib/utils.py

**Checkpoint**: All user stories US1, US2, US3, and US4 should now be independently functional

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Enable users to delete tasks to keep their task list clean and focused on relevant items

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the list, delivering the value of list management.

### Tests for User Story 5 ⚠️

- [ ] T032 [P] [US5] Unit test for delete_task functionality in tests/unit/test_task_manager.py
- [ ] T033 [P] [US5] Integration test for deleting tasks via CLI in tests/integration/test_cli.py

### Implementation for User Story 5

- [ ] T034 [US5] Implement delete_task method in src/services/task_manager.py
- [ ] T035 [US5] Add CLI command for deleting tasks in src/cli/main.py
- [ ] T036 [US5] Add confirmation prompts for task deletion in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: CLI Integration and Error Handling

**Goal**: Integrate all functionality into a cohesive CLI interface with proper error handling

- [ ] T037 [P] Implement main CLI loop in src/cli/main.py
- [ ] T038 [P] Map all commands (add, view, update, delete, complete) to corresponding functions
- [ ] T039 [P] Implement help and exit commands in src/cli/main.py
- [ ] T040 [P] Add error handling for invalid operations in src/cli/main.py
- [ ] T041 [P] Add error messages for non-existent tasks in src/lib/utils.py

---

## Phase 9: Edge Cases and Validation

**Goal**: Handle all edge cases identified in the specification

- [ ] T042 Implement validation for non-existent tasks during update/delete operations
- [ ] T043 Implement validation for empty or invalid task descriptions
- [ ] T044 Handle attempts to mark already completed tasks as complete
- [ ] T045 Handle commands with missing parameters
- [ ] T046 Add comprehensive error handling for all operations

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T047 [P] Add docstrings for all functions and classes
- [ ] T048 Code cleanup and refactoring for readability
- [ ] T049 [P] Additional unit tests in tests/unit/
- [ ] T050 Run quickstart.md validation
- [ ] T051 Final integration testing of all features

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **CLI Integration (Phase 8)**: Depends on all user stories being complete
- **Edge Cases (Phase 9)**: Depends on all user stories being complete
- **Polish (Phase 10)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services
- Services before CLI endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Tasks)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test US1 and US2 together - this is the MVP!
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add US1 + US2 → Test together → Deploy/Demo (MVP!)
3. Add US3 → Test independently → Deploy/Demo
4. Add US4 → Test independently → Deploy/Demo
5. Add US5 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
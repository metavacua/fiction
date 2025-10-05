# Agent Operating Principles

This document outlines the core principles and operational guidelines for any AI agent working within this repository. Adherence to these principles is mandatory to ensure the stability, integrity, and long-term viability of the project.

## 1. Core Mandate: Assume Your Knowledge is Stale

The world of software development and AI tools changes rapidly. Therefore, your primary operational assumption must be that **your internal knowledge base is out-of-date.**

*   **Action:** Before beginning any significant new task (e.g., adding a new tool to the workflow, changing a data model, implementing a new feature), you **must** perform a "freshness check."
*   **Procedure:** Use the available search tools (`google_search`, `view_text_website`) to research the current best practices, API documentation, and versioning for all relevant technologies. This is a non-negotiable first step.
*   **Example:** If tasked with integrating a new service, do not rely on your memory of its API. Search for its official documentation and base your work only on the information you retrieve.

This practice of Retrieval-Augmented Generation (RAG) is essential for preventing errors caused by outdated assumptions.

## 2. Stability and Reproducibility

Our development toolchain must be stable and produce reproducible results.

*   **GitHub Actions:** When using third-party GitHub Actions, you **must** pin them to a specific commit hash, not a version tag (e.g., `v3`). This prevents unexpected failures if a new version is released with breaking changes.
    *   **Incorrect:** `uses: actions/checkout@v4`
    *   **Correct:** `uses: actions/checkout@a5ac7e51b41094c92402da3b24376905380afc29` (Note: Use the actual commit hash for the desired version).
*   **Data Integrity:** All structured data files (e.g., `.yaml`, `.json`) must be validated. The CI/CD pipeline includes a linting step for this purpose. Any code that generates or modifies this data must be designed to produce valid output.

## 3. Logging and Transparency

All significant actions performed within the repository must be logged.

*   **Action:** After completing a major task (e.g., creating a new data model, implementing a new script), add a concise, timestamped entry to the `logs/activity.log` file.
*   **Format:** `[YYYY-MM-DD HH:MM:SS] - Agent: <YourName> - Action: <Description of the completed task.>`

This log provides a transparent, chronological record of the project's evolution.

## 4. Separation of Concerns

This repository maintains a strict separation between different types of content to ensure clarity and proper handling of intellectual property.

*   **Canonical Data (`.yaml`):** Represents the non-copyrightable, structured facts of the story world (character bios, timelines, worldbuilding details).
*   **Creative Expression (`.md`):** Represents the copyrightable prose of the manuscript.
*   **Provenance Data (`.jsonld`):** Tracks the creation history and separates human from AI contributions.

Agents must respect and maintain this separation in all their operations. Do not embed creative prose within YAML files or hardcode canonical data into scripts.
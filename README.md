# An Integrated Writing Workflow with GitHub, SudoWrite, World Anvil & Notion

This repository provides a framework for a modern, integrated writing process, leveraging the power of AI-assisted writing, dedicated worldbuilding tools, and flexible knowledge management, all version-controlled through Git and GitHub.

## The Tools

This workflow integrates the following tools, each with a specific purpose:

*   **GitHub:** The central hub for your project. It provides version control for your manuscript, a place for collaboration and feedback (Issues, Pull Requests), and the automation backbone (GitHub Actions).
*   **SudoWrite:** Your AI writing partner. Used for brainstorming, outlining, drafting, and revising your manuscript with the help of powerful AI features. Its key feature for this workflow is the **Story Bible**, which keeps the AI's writing consistent with your world's lore.
*   **World Anvil:** Your structured worldbuilding database. This is where you create the canonical lore for your world—characters, locations, timelines, magic systems, etc. Its powerful API allows us to sync this information with other tools.
*   **Notion:** Your flexible knowledge base and project management tool. Used for initial, free-form brainstorming, mood boards, research notes, and tracking the overall progress of your project. Its API allows for integration with your central repository.

## The Conceptual Workflow

This workflow is designed to be a cyclical process, allowing you to move between stages as your story develops.

### Stage 1: Ideation & Worldbuilding (Notion & World Anvil)

1.  **Brainstorming (Notion):** Start your project in Notion. Use it as a free-form canvas to dump ideas, create mood boards, gather research, and sketch out initial plot points. The goal here is unrestricted creativity.
2.  **Structuring the Lore (World Anvil):** Once your ideas start to solidify, move the core worldbuilding elements into World Anvil. Create detailed, structured articles for your characters, locations, history, and rules of your world. This becomes the "single source of truth" for your lore.
    *   **Integration Point:** The World Anvil API can be used to create or update articles programmatically.

### Stage 2: Outlining (SudoWrite)

1.  **Create Your Story Bible (SudoWrite):** Use SudoWrite's **Story Bible** feature to define your main characters, synopsis, and key plot points.
    *   **Integration Point:** A script could be created to pull key information from World Anvil's API and populate the SudoWrite Story Bible, ensuring consistency between your lore and your writing AI.
2.  **Generate the Outline:** Use SudoWrite's outlining tools, informed by your Story Bible, to generate a detailed chapter-by-chapter outline for your story.

### Stage 3: Drafting (SudoWrite & GitHub)

1.  **Write Your Manuscript (SudoWrite):** Write your story in SudoWrite, leveraging its AI features like "Write", "Describe", and "Expand" to accelerate the process. The AI will use the information from your Story Bible to maintain consistency.
2.  **Commit to GitHub:** Regularly export your manuscript from SudoWrite (ideally in a plain text format like Markdown) and commit it to this GitHub repository. This creates a version history of your work.
    *   **Best Practice:** Save each chapter as a separate file (e.g., `01-chapter-one.md`) in the `manuscript/` directory. This makes it easier to track changes.

### Stage 4: Review & Collaboration (GitHub)

1.  **Feedback Loop (Issues):** Use GitHub Issues to track feedback from beta readers, editors, or your future self. You can create an issue for a high-level problem (e.g., "The pacing in Act 2 is too slow") or a specific change ("Fix typo in Chapter 3").
2.  **Editing (Branches & Pull Requests):** For significant revisions, create a new branch. Make your changes on that branch, and when you're ready, open a Pull Request. This allows you to see all your changes in one place before merging them into your main manuscript.

### Stage 5: Automation (GitHub Actions)

This is where the workflow becomes truly powerful. A GitHub Action can be created to automate tasks and keep your tools in sync.

*   **Nightly Sync:** A scheduled GitHub Action could run a script that:
    1.  Fetches the latest character and location data from the World Anvil API.
    2.  Updates a summary page in your Notion workspace.
    3.  Perhaps even updates the SudoWrite Story Bible if an API becomes available.
*   **Manuscript Generation:** An action could be triggered to automatically compile all the chapter files in the `manuscript/` directory into a single document (e.g., a `.docx` or `.epub` file) using a tool like Pandoc.

## A Data Model for Creative Provenance

To address the important legal and ethical questions surrounding AI-assisted creation, this project proposes a data model for tracking **Creative Provenance**. The goal is to clearly distinguish between human-authored contributions (which are copyrightable) and AI-generated suggestions (which are not).

This allows for a transparent and auditable record of how every part of the manuscript was created.

The data model is defined by:
*   **[An Ontology](./copyright-datamodel/ONTOLOGY.md):** Defines the core concepts like `AuthorPrompt`, `AIGeneratedSuggestion`, `AuthorSelection`, and `AuthorEdit`.
*   **[A Human-Readable Example](./copyright-datamodel/human-readable-example.yaml):** Shows the model in a clear, step-by-step YAML format.
*   **[A Machine-Readable Example](./copyright-datamodel/machine-readable-example.jsonld):** Provides a semantic JSON-LD version for automated systems.

This model provides a robust framework for managing intellectual property in a collaborative human-AI writing process.

## Proposed Repository Structure

*   **`.github/workflows/`**: This directory will contain the GitHub Actions automation files (e.g., `main.workflow`).
*   **`copyright-datamodel/`**: Contains the ontology and examples for the creative provenance data model.
*   **`manuscript/`**: The main text of your story, with one file per chapter.
*   **`world-anvil-sync/`**: A directory to hold scripts and data related to syncing with World Anvil.
*   **`notes/`**: General project notes that don't fit into the structured lore of World Anvil.
*   **`README.md`**: This file, outlining the workflow.
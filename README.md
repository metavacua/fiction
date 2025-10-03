# Your Next Masterpiece: A Git-Powered Fiction Repository

Welcome to your new writing environment! This repository is set up to help you use the power of Git and GitHub to write, manage, and version your fiction.

## Why Use Git for Writing?

Using a version control system like Git might seem unusual for creative writing, but it offers some incredible benefits:

*   **Infinite History:** Every change you save is recorded. You can go back to any previous version of your work without ever having to worry about `MyStory_v2_final_final.docx` again.
*   **Safe Experimentation:** Want to try a different plot direction or rewrite a chapter? Create a "branch" and experiment freely. If you don't like it, you can discard it without affecting your main story. If you do, you can merge it back in.
*   **Collaboration:** If you work with an editor, beta readers, or a co-author, Git's collaboration tools are unparalleled.
*   **Peace of Mind:** Your work is safely backed up on GitHub.

## Repository Structure

This repository is organized into a few key folders:

*   **`manuscript/`**: This is where the main text of your story lives. It's recommended to break your story into smaller files, like one file per chapter.
*   **`character-notes/`**: A place to keep all your character sketches, backstories, and development notes.
*   **`world-building/`**: For all the details about your story's world, including locations, concepts, and rules.
*   **`templates/`**: Contains templates for creating new character profiles and world-building entries to ensure consistency.
*   **`dist/`**: This is where output files (like `.docx` versions of your manuscript) are saved. This folder is ignored by Git.

## Using the Templates

To keep your notes organized, you can use the templates provided in the `templates/` folder:

*   `templates/character-template.md`: For creating new character profiles.
*   `templates/world-building-template.md`: For creating new world-building entries.

Simply copy the template into the appropriate directory (e.g., `character-notes/`) and fill it out.

## Building Your Manuscript

This repository includes a script to compile all your chapter files from the `manuscript/` directory into a single document.

1.  **File Naming:** To ensure your chapters are compiled in the correct order, you **must** name your files sequentially using a leading number. For example:
    *   `01-prologue.md`
    *   `02-chapter-one.md`
    *   `03-chapter-two.md`
    *   ...etc.
2.  **Prerequisites:** You need to have [Pandoc](https://pandoc.org/installing.html) installed on your system.
3.  **Run the script:** From your terminal, run the following command:
    ```bash
    ./build.sh
    ```
4.  **Find the output:** The script will combine all manuscript files into a single `manuscript.docx` file in the `dist/` directory.

## Best Practice: Use Plain Text

**This is the most important tip.** Git is designed to work with plain text files. This means formats like Markdown (`.md`), Fountain (`.fountain` for screenplays), or even just plain `.txt`.

**Why not `.docx` or other rich text formats?**

Files like `.docx` or `.pages` are actually complex compressed files (like a `.zip`). When you make a small change, like fixing a typo, Git sees the *entire file* as changed. This means:

*   You can't easily see *what* changed (the "diff").
*   You lose the ability to intelligently merge different versions.
*   The repository size can balloon quickly.

Markdown (`.md`) is a great choice because it's simple to learn, readable as plain text, and can be easily converted to other formats like `.epub` or `.pdf` when you're ready to publish.

Happy writing!
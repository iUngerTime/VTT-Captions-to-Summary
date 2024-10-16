# README: VTT Transcript Summarizer

## Fun Disclaimer

_Most of this codebase was ChatGPT generated! Documentation, code snippets, git commits, etc. It was heavily directed. Finished in about 3 hours total, by a sleepy dev._

## Description

The VTT Transcript Summarizer is an application that takes in a `.vtt` file, particularly from Microsoft Teams, cleans and processes it, and then provides a concise recap using the OpenAI's GPT-3.5-turbo model. The application extracts the essence of a transcript, highlighting key points, action items, and unanswered questions. This is particularly useful for those looking to quickly understand the outcomes of meetings without having to go through the entire transcript.

## Features

- Reads and cleans `.vtt` files to remove timestamps and unnecessary metadata.
- Summarizes transcripts into bullet points that capture key points, action items, or unanswered questions.
- Provides a final, organized summarization to present the findings.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/iUngerTime/VTT-Captions-to-Summary.git
   cd <repository_directory>
   ```

2. **Install the necessary libraries**:

   ```bash
   pip install openai tiktoken python-dotenv
   ```

3. **Setup OpenAI credentials**:
   - Copy example `.env.example` file to `.env` in root of directory
   - Replace `<your_openai_api_key>` with your OpenAI secret generated in your profile settings on <https://platform.openai.com/>

## Running the Application

1. **Run the application**:

   ```bash
   python3 <script_name>.py
   ```

## Usage

- Ensure your `.vtt` file is ready. Update the `file_path` variable in the script to reflect your location.

- Run the application as instructed above. The script will process the `.vtt` file and provide a summarized recap in the console.

## Notes

- Token usage and limits have been taken into consideration. Large transcripts are batch processed to fit within OpenAI's token limit.
- Always remember that the accuracy and quality of the summarization can vary. Always review and adjust the results/prompts as needed. I hold zero responsibility for the output of the program!
- Microsoft does not attach the people's names to the individual commenting in the transcript. If that functionality exists, or your VTT file has those, consider updating the cleaning function to properly check it.
- The default microsoftTeamsGeneratedTranscript.vtt has been added to .gitignore so you don't accidentally publish private corporate information into a public repository. :)

## Dependencies

- OpenAI: For using the GPT-3.5-turbo model to generate summaries.
- Tiktoken: For counting how many tokens are in a text string without making an API call.
- python-dotenv: For loading environment variables from an `.env` file.

## Feedback and Contributions

- For feedback, issues, or contributions, please open an issue or pull request on the repository.

## License

- This project is open-source and available to everyone. Please ensure to credit the original author when sharing or using in your projects.

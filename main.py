import gradio as gr 


# Define dictionaries for purposes
purpose = {
    "Comprehensive": "\nWrite a detailed and thorough article that covers all aspects of the topic, providing in-depth information and analysis to ensure a comprehensive understanding for the readers, ",
    "Convincing": "\nWrite a persuasive and well-supported article that presents compelling arguments, backed by credible \"\"\"facts\"\"\" and logical reasoning, to effectively convince the readers of the topic, ",
    "Problem-Solving": "\nWrite a practical and solution-focused article that identifies common problems, offers step-by-step guidance, and provides actionable advice to help readers effectively resolve these issues, ",
    "Inspiring": "\nWrite an uplifting and motivational article that shares powerful stories, encouraging words, and positive messages to inspire and energize readers to pursue their goals and dreams, ",
    "Entertaining": "\nWrite an engaging and enjoyable article filled with captivating stories, humorous anecdotes, and intriguing facts to entertain and delight the readers, "
}

# Define dictionaries for document formats
document_format = {
    "Memo": "\nFormat your writing to be a memo, including a header with 'To,' 'From,' 'Date,' and 'Subject' lines, followed by a concise body text that clearly conveys the main points, and a concluding section with any necessary action items or next steps.",
    "Blog Post": "\nFormat your writing to be a blog post, with a catchy headline, relevant images or multimedia, and a call to action or invitation for reader comments.",
    "Grant Proposal": "\nFormat your writing to be a grant proposal that includes an executive summary, a detailed needs assessment, a clear project description, specific goals and objectives, a thorough methodology, a detailed budget, and an evaluation plan to effectively communicate the project's purpose and funding requirements.",
    "Environmental Impact Assessment": "\nFormat your writing to be a comprehensive Environmental Impact Assessment (EIA) article that thoroughly examines the potential environmental effects of the proposed project, including detailed evaluations of the ecological, social, and economic impacts, supported by data and evidence, and offering informed recommendations for mitigation and sustainability.",
    "Marketing Brochure": "\nFormat your writing to be a compelling marketing brochure that effectively highlights the key benefits and unique features of the product, engaging potential customers with persuasive language, eye-catching visuals, and a strong call to action."
}

# Define dictionaries for audiences
audience = {
    "Public Audience": "\nWrite in simple terms that anyone can understand, appealing to public audience.",
    "Children": "\nPlease write in a very simple language, using short sentences and easy words, as if you are talking to a child under 10 years old. Make sure to break down complex ideas into simple concepts and use examples that a young child would understand.",
    "Donors": "\nWrite the article specifically tailored for donating organizations, addressing their interests and priorities, and ensuring the content is relevant and compelling to this audience."
}

# Define dictionaries for tone
advanced_tone = {
    "Neutral": "\nYour writing must maintain a completely objective and fact-based tone, ensuring neutrality throughout and avoiding any bias or unsupported information.",
    "Friendly": "\nYour writing must maintain a highly friendly tone, ensuring the language is warm, inviting, and personable, making the reader feel genuinely welcomed and engaged, as though having a pleasant conversation with a close friend.",
    "Informal": "\nYour writing must maintain a highly informal tone, using laid-back and conversational language to ensure the content feels relatable and easy to read as if discussing the topic with a close acquaintance.",
    "Informal and Modest": "\nYour writing must maintain an informal yet highly neutral tone, using straightforward, conversational language to ensure the content is engaging and accessible, while strictly maintaining objectivity and avoiding bias or exaggeration.",
    "Friendly and Modest": "\nYour writing must maintain a friendly and neutral tone, using approachable language to engage the reader, while ensuring all information is fact-based."
}
paragraphs_order_dict = {
    1: "First",
    2: "Second",
    3: "Third", 
    4: "Forth", 
    5: "Fifth", 
    6: "Sixth"}

avoid_list = ["Too many exaggerated or advertising phrases",
              "Promotional language and exaggerated words", 
              "Too many exaggerated phrases"]

# Function to generate the simple prompt

def generate_simple_prompt(simple_topic, simple_tone, simple_avoid, simple_nb_of_words, simple_para1, simple_para2, simple_para3, simple_para4, simple_para5, simple_para6, simple_with_attachment):
    
    try:
        simple_prompt = "Please act as a professional press release writer.\n"
        
        # Topic
        if len(simple_topic) > 0:
            simple_prompt += f"Write a press release about \"\"\"{simple_topic}\"\"\"\n"

            # Tone and avoid
            if not simple_tone == None:
                if not simple_avoid == None:
                    simple_prompt += f"Your writing must maintain a {simple_tone.lower()} tone, avoiding {simple_avoid.lower()}.\n"
                else:
                    simple_prompt += f"Your writing must maintain a {simple_tone.lower()} tone.\n"
                    
            # Attachment
            if simple_with_attachment:
                simple_prompt += "Use the attached files as a reference.\n"
            # Structure
            simple_para_new_list = []
            paragraphs = [simple_para1, simple_para2, simple_para3, simple_para4, simple_para5, simple_para6]
            for i, para in enumerate(paragraphs, start=1):
                if len(para) > 0:
                    simple_para_new_list.append(para)
          
            if len(simple_para_new_list) > 0:
                simple_prompt += "Follow the below structure: \n\"\"\""
                simple_para_order = 1
                for para in simple_para_new_list:
                    if simple_para_new_list.index(para) == len(simple_para_new_list)-1:
                        simple_prompt += f"{paragraphs_order_dict[simple_para_order]} paragraph: {para}"
                    else:
                        simple_prompt += f"{paragraphs_order_dict[simple_para_order]} paragraph: {para}\n"
                    simple_para_order += 1
                simple_prompt += "\"\"\"\n"

            #article length
            if simple_nb_of_words > 0:
                simple_prompt += f"Make sure to write up to {simple_nb_of_words} words."
                
            
            
            return simple_prompt
        else:
            return "Please fill the topic field first!"
      
    except Exception as e:
        raise gr.Error(repr(e))



# Define the function to generate the prompt
def generate_advanced_prompt(purpose_value, advanced_topic, document_format_value, accept_format_structure, advanced_para1_title, advanced_para2_title, advanced_para3_title, advanced_para4_title, advanced_para5_title, advanced_para6_title, advanced_tone_value, audience_value, advanced_avoid, advanced_max_nb_words, advanced_with_attach_input):
    
  
    advanced_prompt = "Please act as a professional article writer." + purpose[purpose_value]

    try:

      #topic
      if len(advanced_topic) > 0:
            advanced_prompt += f"about {advanced_topic}."
            
            #document format, tone, and audience
            advanced_prompt += document_format[document_format_value] + advanced_tone[advanced_tone_value] + audience[audience_value]
            #avoid
            if not advanced_avoid == None:
                  advanced_prompt += f"\nYou must avoid {advanced_avoid.lower()}"
                  
            # Structure
            if not accept_format_structure:
                  advanced_para_new_list = list()
                  advanced_paragraphs = [advanced_para1_title, advanced_para2_title, advanced_para3_title, advanced_para4_title, advanced_para5_title, advanced_para6_title]
                  for para in advanced_paragraphs:
                        if len(para) > 0:
                            advanced_para_new_list.append(para)
                          
                  if len(advanced_para_new_list) > 0:
                        advanced_prompt += "\nFollow the below structure: \n\"\"\""
                        advanced_para_order = 1
                        for para in advanced_para_new_list:
                            if advanced_para_new_list.index(para) == len(advanced_para_new_list)-1:
                                advanced_prompt += f"{paragraphs_order_dict[advanced_para_order]} paragraph: {para}."
                            else:
                                advanced_prompt += f"{paragraphs_order_dict[advanced_para_order]} paragraph: {para}.\n"
                            advanced_para_order += 1
                        advanced_prompt += "\"\"\" "
            #article length
            if advanced_max_nb_words > 0:
                  advanced_prompt += f"\nMake sure to write up to {advanced_max_nb_words} words."
            #SEO optimization
            if advanced_with_attach_input:
                  advanced_prompt += "\nUse the attached files as a reference.\nBoost your SEO by extracting keywords from the attached files."
            return advanced_prompt
      else:
        return "Please fill the topic field first!!"
    except Exception as e:
        raise gr.Error(repr(e))

with gr.Blocks(theme=gr.themes.Base(neutral_hue="indigo", text_size = gr.themes.sizes.text_lg)) as app:
    
    gr.Markdown("> ## ChatGPT Prompt Generator for Creative Writing")
    with gr.Tabs():
        with gr.TabItem("Simple Prompt Generator"):
            with gr.Row():
                with gr.Column():
                    simple_topic_input = gr.Textbox(label="Topic")
                with gr.Column():
                    simple_tone_input = gr.Dropdown(["Modest"], label="Tone")
            with gr.Row():
                with gr.Column():
                    simple_avoid_input = gr.Dropdown(choices=avoid_list, label="Avoid")
                with gr.Column():
                    simple_nb_of_words_input = gr.Number(label="Maximum Number of Words")
                with gr.Column():
                    simple_with_attach_input = gr.Checkbox(label="With attachment", info="Check if you would like to use resource files along with the generated prompt in ChatGPT chatbot", value=False)
            with gr.Row():
                gr.Markdown("> `Specify Exact Structure`")
            with gr.Row():
                with gr.Column():
                    simple_para1_input = gr.Textbox(label="First Paragraph:")
                with gr.Column():
                    simple_para2_input = gr.Textbox(label="Second Paragraph:")
                with gr.Column():
                    simple_para3_input = gr.Textbox(label="Third Paragraph:")
            with gr.Row():
                with gr.Column():
                    simple_para4_input = gr.Textbox(label="Fourth Paragraph:")
                with gr.Column():
                    simple_para5_input = gr.Textbox(label="Fifth Paragraph:")
                with gr.Column():
                    simple_para6_input = gr.Textbox(label="Sixth Paragraph:")
            with gr.Row():
                with gr.Column():
                    simple_generate_button = gr.Button("Generate Simple Prompt")
                with gr.Column():
                    simple_clear_button = gr.ClearButton([simple_topic_input, simple_tone_input, simple_avoid_input, simple_nb_of_words_input, simple_with_attach_input, simple_para1_input, simple_para2_input, simple_para3_input, simple_para4_input, simple_para5_input, simple_para6_input])
            with gr.Row():
                simple_output_textbox = gr.Textbox(label="Generated Simple Prompt", show_copy_button=True, lines=20)

        with gr.TabItem("Advanced Prompt Generator"):
            with gr.Row():
                with gr.Column():
                    purpose_input = gr.Dropdown(label="Purpose", choices=list(purpose.keys()), value=list(purpose.keys())[0])
                with gr.Column():
                    advanced_topic_input = gr.Textbox(label="Topic")
            with gr.Row():
                with gr.Column():
                    document_format_input = gr.Dropdown(label="Document Format", choices=list(document_format.keys()), value=list(document_format.keys())[0])
                with gr.Column():
                    advanced_tone_input = gr.Dropdown(label="Tone", choices=list(advanced_tone.keys()), value=list(advanced_tone.keys())[0])
            with gr.Row():
                with gr.Column():
                    audience_input = gr.Dropdown(label="Audience", choices=list(audience.keys()), value=list(audience.keys())[0])
                with gr.Column():
                    advanced_max_nb_words_input = gr.Number(label="Maximum Number of Words")
            with gr.Row():
                with gr.Column():
                    advanced_with_attach_input = gr.Checkbox(label="With attachment", info="Check if you would like to use resource files along with the generated prompt in ChatGPT chatbot", value=False)
                with gr.Column():
                    advanced_avoid_input = gr.Dropdown(choices=avoid_list, label="Avoid")
            with gr.Row():
                accept_format_structure_input = gr.Checkbox(label="Accept the Document Format Structure", info="Check if you would like to accept the ", value=False)
            gr.Markdown("> `Specify Exact Structure`")
            with gr.Row():
                with gr.Column():
                    advanced_para1_input = gr.Textbox(label="First Paragraph:")
                with gr.Column():
                    advanced_para2_input = gr.Textbox(label="Second Paragraph:")
                with gr.Column():
                    advanced_para3_input = gr.Textbox(label="Third Paragraph:")
            with gr.Row():
                with gr.Column():
                    advanced_para4_input = gr.Textbox(label="Fourth Paragraph:")
                with gr.Column():
                    advanced_para5_input = gr.Textbox(label="Fifth Paragraph:")
                with gr.Column():
                    advanced_para6_input = gr.Textbox(label="Sixth Paragraph:")
            with gr.Row():
                with gr.Column():
                    advanced_generate_button = gr.Button("Generate Advanced Prompt")
                with gr.Column():
                    advanced_clear_button = gr.ClearButton([purpose_input, advanced_topic_input, document_format_input, advanced_tone_input, audience_input, advanced_max_nb_words_input, advanced_with_attach_input, advanced_avoid_input, accept_format_structure_input, advanced_para1_input, advanced_para2_input, advanced_para3_input, advanced_para4_input, advanced_para5_input, advanced_para6_input])
            with gr.Row():
                advanced_output_textbox = gr.Textbox(label="Generated Advanced Prompt", show_copy_button=True, lines=20)
    gr.Markdown(
    """ Copyright (c) 2024 KIC  
    This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.  
    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  
    You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.""")
    simple_generate_button.click(generate_simple_prompt, inputs=[simple_topic_input, 
                        simple_tone_input, 
                        simple_avoid_input, 
                        simple_nb_of_words_input,
                        simple_para1_input,
                        simple_para2_input,
                        simple_para3_input,
                        simple_para4_input,
                        simple_para5_input,
                        simple_para6_input,
                        simple_with_attach_input], outputs=simple_output_textbox)
    advanced_generate_button.click(generate_advanced_prompt, inputs=[purpose_input, 
                advanced_topic_input, 
                document_format_input, 
                accept_format_structure_input,
                advanced_para1_input,
                advanced_para2_input,
                advanced_para3_input,
                advanced_para4_input,
                advanced_para5_input,
                advanced_para6_input,
                advanced_tone_input, 
                audience_input, 
                advanced_avoid_input, 
                advanced_max_nb_words_input, 
                advanced_with_attach_input,], outputs=advanced_output_textbox)

if __name__ == "__main__":
    app.launch(share=True)
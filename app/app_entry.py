from app.agents.crew import MedicalAssistantCrew
from app.agents.tools.pdf_reader_tool import text_from_pdf as pdf_reader
from app.agents.tools.ocr_reader import text_from_image as ocr_reader
import gradio as gr

crew_instance = MedicalAssistantCrew().medical_assistant_crew()

class MedicalAssistantApp():

    def process_report(report_file, symptoms):

        report_text = pdf_reader(report_file.name)

        result = crew_instance.kickoff(
            inputs={
                "medical_report": report_text,
                "symptoms": symptoms
            }
        )

        return result

    def process_medicine_image(image_file, symptoms):

        medicine_text = ocr_reader(image_file)

        result = crew_instance.kickoff(
            inputs={
                "medicine_text": medicine_text,
                "symptoms": symptoms
            }
        )

        return result



    def process_symptoms(symptoms):

        result = crew_instance.kickoff(
            inputs={
                "symptoms": symptoms
            }
        )

        return result


    with gr.Blocks() as demo:

        gr.Markdown("# AI Medical Assistant")


        with gr.Tab("Medical Report"):

            report_file = gr.File(label="Upload Medical Report")
            report_symptoms = gr.Textbox(label="Optional Symptoms")
            report_output = gr.Textbox(label="Analysis Result", lines=20)

            report_btn = gr.Button("Analyze Report")

            report_btn.click(
                fn=process_report,
                inputs=[report_file, report_symptoms],
                outputs=report_output
            )


        with gr.Tab("Medicine Analysis"):

            medicine_image = gr.Image(type="filepath", label="Upload Medicine Image")
            medicine_symptoms = gr.Textbox(label="Optional Health Condition")
            medicine_output = gr.Textbox(label="Medicine Analysis", lines=20)

            medicine_btn = gr.Button("Analyze Medicine")

            medicine_btn.click(
                fn=process_medicine_image,
                inputs=[medicine_image, medicine_symptoms],
                outputs=medicine_output
            )


        with gr.Tab("Symptom Checker"):

            symptom_input = gr.Textbox(label="Describe Symptoms", lines=5)
            symptom_output = gr.Textbox(label="Possible Conditions", lines=20)

            symptom_btn = gr.Button("Analyze Symptoms")

            symptom_btn.click(
                fn=process_symptoms,
                inputs=[symptom_input],
                outputs=symptom_output
            )


    demo.launch(share=True)


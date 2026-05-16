from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.project import CrewBase, agent, task, crew
load_dotenv()

llm = LLM(
    model = "openrouter/deepseek/deepseek-chat",
    temperature = 0.7
)

@CrewBase
class MedicalAssistantCrew():
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def report_analysis_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['report_analysis_agent'],
            llm = llm
        )
    
    @agent
    def medical_value_evaluator(self) -> Agent:
        return Agent(
            config = self.agents_config['medical_value_evaluator'],
            llm = llm
        )
    
    @agent
    def medicine_ocr_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['medicine_ocr_agent'],
            llm = llm
        )
    
    @agent
    def medicine_research_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['medicine_research_agent'],
            llm = llm
        )
    
    @agent
    def symptom_analyzer_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['symptom_analyzer_agent'],
            llm = llm
        )
    
    @agent
    def treatment_suggestion_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['treatment_suggestion_agent'],
            llm = llm
        )
    
    @agent
    def supervisor_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['supervisor_agent'],
            llm = llm
        )
    


    # TASKS

    @task
    def analyze_medical_report_task(self) -> Task:
        return Task(config=self.tasks_config['analyze_medical_report_task'])


    @task
    def evaluate_medical_values_task(self) -> Task:
        return Task(config=self.tasks_config['evaluate_medical_values_task'])


    @task
    def extract_medicine_text_task(self) -> Task:
        return Task(config=self.tasks_config['extract_medicine_text_task'])


    @task
    def research_medicine_task(self) -> Task:
        return Task(config=self.tasks_config['research_medicine_task'])


    @task
    def analyze_symptoms_task(self) -> Task:
        return Task(config=self.tasks_config['analyze_symptoms_task'])


    @task
    def generate_treatment_guidance_task(self) -> Task:
        return Task(config=self.tasks_config['generate_treatment_guidance_task'])


    @task
    def generate_final_response_task(self) -> Task:
        return Task(config=self.tasks_config['generate_final_response_task'])


   
    # CREW
    

    @crew
    def medical_assistant_crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            verbose=True
        )
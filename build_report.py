from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path

OUT = Path('output/pdf/Smart_Task_Priority_Predictor_Project_Report.pdf')
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE = colors.HexColor('#17365D')
MID_BLUE = colors.HexColor('#DCE6F1')
LIGHT = colors.HexColor('#F4F7FA')
GRAY = colors.HexColor('#666666')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='RptTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=24,
    leading=30, textColor=colors.black, alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name='SubTitle', parent=styles['Normal'], fontName='Helvetica', fontSize=12,
    leading=18, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name='H1x', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=17,
    leading=21, textColor=colors.black, spaceBefore=2, spaceAfter=12, keepWithNext=True))
styles.add(ParagraphStyle(name='H2x', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12,
    leading=15, textColor=colors.black, spaceBefore=9, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name='Bodyx', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.1,
    leading=15, alignment=TA_JUSTIFY, spaceAfter=8))
styles.add(ParagraphStyle(name='Small', parent=styles['BodyText'], fontName='Helvetica', fontSize=8.8,
    leading=12, alignment=TA_LEFT, spaceAfter=4))
styles.add(ParagraphStyle(name='Cap', parent=styles['BodyText'], fontName='Helvetica-Oblique', fontSize=8.8,
    leading=11, alignment=TA_CENTER, textColor=GRAY, spaceBefore=4, spaceAfter=8))

def P(text, style='Bodyx'):
    return Paragraph(text, styles[style])

def bullet(text):
    return P('&bull; ' + text)

def tbl(rows, widths, header=True, small=False):
    data=[]
    for row in rows:
        data.append([P(str(c), 'Small' if small else 'Bodyx') for c in row])
    t=Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    commands=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#D9D9D9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
              ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
              ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]
    if header:
        commands += [('BACKGROUND',(0,0),(-1,0),BLUE),('TEXTCOLOR',(0,0),(-1,0),colors.white),
                     ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('BACKGROUND',(0,1),(-1,-1),LIGHT)]
    t.setStyle(TableStyle(commands))
    return t

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#D9D9D9')); canvas.line(45, 40, A4[0]-45, 40)
    canvas.setFont('Helvetica',8); canvas.setFillColor(GRAY)
    canvas.drawString(45,27,'Smart Task Priority Predictor - Project Report')
    canvas.drawRightString(A4[0]-45,27,f'Page {doc.page}')
    canvas.restoreState()

story=[]
# 1
story += [Spacer(1,0.55*inch), P('SMART TASK PRIORITY PREDICTOR','RptTitle'),
          P('Project Report','SubTitle'), Spacer(1,0.18*inch),
          P('A Flask-based task management system with rule-based scoring and basic machine learning classification. The application assists users in identifying tasks that need immediate attention by considering deadline, urgency, business impact, effort, and dependencies.','Bodyx'), Spacer(1,0.22*inch),
          tbl([['Submitted by','SANJAY S'],['Email ID','sanjayss007700@gmail.com'],['Intern ID','SHA20260724WB7B566C24INTERN'],['College','JCT COLLEGE OF ENGINEERING AND TECHNOLOGY']], [1.75*inch,4.55*inch], header=False),
          Spacer(1,0.34*inch), P('ABSTRACT','H1x'),
          P('Task prioritization is a practical problem for students, project teams, and individual users. When many tasks compete for attention, decisions made only by memory or intuition can be inconsistent. Smart Task Priority Predictor provides a clear, repeatable process for creating tasks, evaluating their priority, and tracking the result. The system combines an understandable weighted scoring formula with a Decision Tree classifier. It presents a priority label - Low, Medium, High, or Critical - together with a score and simple reasons for the decision. The project is intentionally designed at an intermediate level, using Python, Flask, SQLite, Pandas, Scikit-learn, HTML, CSS, and Pytest. It also supports manual priority overrides and CSV batch prediction, allowing a user to retain control while benefiting from a structured recommendation.'),
          Spacer(1,0.15*inch), P('Keywords: task management, task priority, Flask, SQLite, Decision Tree, machine learning, CSV batch prediction.','Small'), PageBreak()]
# 2
story += [P('1. Introduction and Problem Statement','H1x'),
          P('Modern work often involves a mixture of urgent requests, high-value activities, dependent tasks, and routine work. A user may know that all tasks are important, yet still struggle to decide which one should be completed first. The difficulty increases when deadlines are close, the business impact is high, or a task blocks other work. A simple task list records work, but it does not always provide a consistent way to rank that work.'),
          P('The Smart Task Priority Predictor addresses this gap through a web application that captures important task characteristics and transforms them into an explainable priority recommendation. The system does not replace human judgement. Instead, it provides a structured baseline so that users can compare tasks using the same criteria every time.'),
          P('1.1 Project Purpose','H2x'),
          P('The purpose of the project is to develop a working Flask application that supports task management and priority prediction. A registered user can create, view, edit, delete, search, filter, and update the status of their own tasks. For each valid task, the application calculates a priority score from 0 to 100 and uses a saved Decision Tree model to predict a priority category. The application displays readable reasons behind the final result and stores prediction history for later review.'),
          P('1.2 Scope','H2x'),
          tbl([['Included in the project','Excluded from the internship version'],['Flask session login, task CRUD, SQLite storage','Cloud deployment, containers, CI/CD pipelines'],['Weighted scoring, Decision Tree classification','OAuth/JWT authentication and enterprise databases'],['CSV upload and batch prediction','External task-management integrations'],['Dashboard counts, basic charts, tests','Deep learning, LLMs, model drift automation']], [3.15*inch,3.15*inch]),
          P('The scope is deliberately limited to technologies that can be developed, tested, and demonstrated locally. This keeps the design focused while still showing essential skills in backend development, databases, data processing, machine learning, and user interface development.'),
          P('1.3 Objectives','H2x'),
          bullet('Build a usable web application for managing personal or project tasks.'), bullet('Generate a transparent priority score and one of four priority labels.'), bullet('Train and integrate a basic Decision Tree model using prepared task data.'), bullet('Provide batch processing, manual overrides, and automated tests.'), PageBreak()]
#3
story += [P('2. System Architecture and Workflow','H1x'),
          P('The system follows a straightforward three-layer design. The presentation layer contains HTML and CSS pages for registration, login, dashboard, task forms, task lists, and batch prediction. The application layer is built with Flask and handles routes, sessions, input validation, task operations, priority calculation, and prediction requests. The data layer uses SQLite to store users, tasks, predictions, and priority overrides. A separate machine learning module loads the saved Scikit-learn model when a prediction is required.'),
          tbl([['Component','Main Responsibility'],['HTML, CSS and Bootstrap interface','Collect task data, display lists, charts, results and validation messages.'],['Flask application','Route handling, session management, validation, CRUD operations and response rendering.'],['Priority rule module','Compute score, map score to label and produce simple explanation messages.'],['Pandas preprocessing module','Read CSV files, clean data, derive days to deadline and encode task type.'],['Scikit-learn model','Classify a task as Low, Medium, High or Critical.'],['SQLite database','Persist users, tasks, predictions and override history.']], [2.0*inch,4.3*inch]),
          P('2.1 Prediction Flow','H2x'),
          P('A user starts by entering a task name, deadline, estimated effort, business impact, urgency, dependency count, task type, and status. Flask validates these values before processing. The system derives the number of days remaining, calculates a rule-based score, and prepares the feature set expected by the saved model. The Decision Tree produces a predicted class. When the model result and the score range disagree, the score range is used as the final category because it remains directly explainable to the user. The resulting label, score, model prediction, and reasons are stored with the task.'),
          P('2.2 Benefits of the Architecture','H2x'),
          P('Separating the web routes, database operations, scoring rules, preprocessing logic, and model code improves maintainability. Each module has a clear responsibility and can be tested independently. For example, changes to the scoring formula can be verified without modifying the user interface, while model retraining can reuse the same preprocessing logic used during prediction. This organization is appropriate for an internship project because it demonstrates clean coding practices without adding unnecessary infrastructure.'), PageBreak()]
#4
story += [P('3. Functional Requirements','H1x'),
          P('The application requirements are organized around user management, task management, prediction, overrides, and batch processing. All operations must be simple enough for a local web application while preserving correct ownership of user data.'),
          tbl([['ID','Requirement'],['FR-01 to FR-04','A user can register with name, email, and password; log in and log out; remain authenticated through a Flask session; and view or modify only their own tasks.'],['FR-05 to FR-11','A user can create, view, edit, delete, search, filter, sort, and update the status of tasks.'],['FR-12 to FR-17','The system calculates a score from 0 to 100, classifies priority, uses a Decision Tree, displays the result and reasons, and stores each prediction.'],['FR-18','A user can manually change the suggested priority after providing an override reason.'],['FR-19','A user can upload a CSV file, receive row-level validation feedback, process valid rows, preview results, and download the result CSV.']], [1.25*inch,5.05*inch]),
          P('3.1 Task Input Validation','H2x'),
          P('Reliable predictions depend on valid inputs. The task name and deadline are mandatory. The deadline must not be earlier than the creation date. Estimated effort must be greater than zero. Business impact and urgency must each be integers from 1 to 10, while dependency count must be zero or greater. Task type is selected from Development, Testing, Design, Documentation, or Other. Status is selected from Not Started, In Progress, Blocked, Completed, or Cancelled.'),
          P('3.2 Expected Error Handling','H2x'),
          tbl([['Situation','Expected system response'],['Missing required value','Show a clear validation message beside the related field.'],['Invalid impact or urgency','Explain that the permitted range is 1 to 10.'],['Invalid effort or deadline','Request a positive effort value or a valid future date.'],['Incorrect login','Show the message: Invalid email or password.'],['Invalid CSV columns','List the missing or incorrect column names.'],['Model or database failure','Show a general service error and record technical details in logs.']], [2.3*inch,4.0*inch]),
          P('Completed tasks do not receive a new priority, and cancelled tasks are excluded from priority ranking. These business rules prevent misleading recommendations for work that is no longer active.'), PageBreak()]
#5
story += [P('4. Priority Calculation Logic','H1x'),
          P('The core of the application is an explainable scoring formula. It is intentionally based on simple arithmetic so that users and developers can understand how each factor affects the result. Business impact has the largest weight, followed by urgency. Dependencies and deadline pressure add further points. Estimated effort is used as a small adjustment rather than the primary decision factor.'),
          P('4.1 Score Formula','H2x'),
          P('<b>Priority Score = (Business Impact x 4) + (Urgency x 3) + (Dependency Count x 2) + Deadline Points + Effort Adjustment</b>'),
          P('After calculation, the value is restricted to the range 0 to 100. A task with impact 9, urgency 9, four dependencies, and a deadline within two days receives 36 + 27 + 8 + 15 = 86 points before effort adjustment. The result is Critical priority.'),
          tbl([['Deadline situation','Points','Reason'],['Overdue','20','Immediate attention is required because the commitment has already passed.'],['Today or within 2 days','15','The task is time-sensitive and should be reviewed quickly.'],['Within 7 days','10','The deadline is approaching and needs planning.'],['Within 14 days','7','The deadline contributes moderate priority pressure.'],['More than 14 days','3','The task has lower deadline pressure.']], [1.85*inch,0.8*inch,3.65*inch]),
          P('4.2 Effort Adjustment and Priority Mapping','H2x'),
          tbl([['Condition','Adjustment or Result'],['Estimated effort below 3 hours','Add 5 points because the task may be a useful quick win.'],['Estimated effort above 20 hours','Subtract 5 points because high effort slightly reduces immediate completion value.'],['Score 80 to 100','Critical'],['Score 60 to 79','High'],['Score 40 to 59','Medium'],['Score 0 to 39','Low']], [2.55*inch,3.75*inch]),
          P('The scoring result is paired with simple messages, such as "Urgency is high and increases the priority" or "The task has several dependencies and may affect other work." These messages help users understand the decision without requiring advanced explainability tools.'), PageBreak()]
#6
story += [P('5. Machine Learning and Data Preparation','H1x'),
          P('The machine learning feature is implemented as a supervised classification problem. A Decision Tree Classifier is selected because it is easy to train, inspect, and explain. It predicts one of four labels: Low, Medium, High, or Critical. The model supplements the rule-based score; it is not intended to be an opaque or autonomous decision-maker.'),
          P('5.1 Dataset and Features','H2x'),
          tbl([['Field','Purpose in the dataset'],['task_id','Unique identifier used to detect duplicate records.'],['created_date and deadline_date','Used to derive days to deadline.'],['estimated_effort','Expected work in hours.'],['business_impact and urgency','Core ratings from 1 to 10.'],['dependency_count','Number of tasks that depend on this work.'],['task_type','Categorical feature encoded into numeric columns.'],['priority_label','Target class used for training.']], [2.15*inch,4.15*inch]),
          P('5.2 Preprocessing Process','H2x'),
          P('Pandas reads the CSV source and verifies that all required columns are available. Date columns are converted to a valid date format, numerical ranges are checked, missing numerical values may be filled using the median, and missing task types are set to Other. Duplicate task identifiers are removed. The system calculates days to deadline and applies one-hot encoding to task type values. The same transformation logic is retained in a separate preprocessing module so that training and live prediction use compatible features.'),
          P('5.3 Training and Evaluation','H2x'),
          P('The dataset is split into 80 percent training data and 20 percent test data. A DecisionTreeClassifier with controlled settings is trained on the prepared features. Its performance is measured on the unseen test data using accuracy, precision, recall, and F1-score. The expected internship target is at least 75 percent accuracy and approximately 70 percent for precision, recall, and F1-score. These are practical targets for a basic synthetic or CSV-based dataset, not production guarantees. The trained model is saved with Joblib for later use by the Flask application.'),
          P('A balanced dataset is important. Each priority category should have enough examples so the model does not learn to favor only the most common label. When the dataset changes substantially, the model should be retrained manually and evaluated again.'), PageBreak()]
#7
story += [P('6. Database Design and Security','H1x'),
          P('SQLite is used as a lightweight relational database for the local version of the system. The schema preserves a clear relationship between users, their tasks, generated predictions, and any manual changes to priority. Foreign-key relationships ensure that prediction and override information remains associated with the correct task.'),
          tbl([['Table','Key information stored'],['Users','user_id, name, unique email, password value, created_at'],['Tasks','task_id, user_id, title, description, deadline, effort, impact, urgency, dependencies, type, status, created_at'],['Predictions','prediction_id, task_id, priority_score, priority_label, model_prediction, created_at'],['Override History','override_id, task_id, original_priority, new_priority, reason, created_at']], [1.55*inch,4.75*inch]),
          P('6.1 Data Relationships','H2x'),
          P('One user can own many tasks. Each task can have a prediction record, and a task may also have one or more override history records if its priority has been changed. The application uses the logged-in user identity to ensure that a user only reads or modifies their own records. This ownership check is essential even in a small local project.'),
          P('6.2 Security Measures','H2x'),
          bullet('Flask sessions maintain login state after successful authentication.'), bullet('Server-side validation checks every form field before it is saved or predicted.'), bullet('Parameterized SQLite queries or an ORM prevent unsafe SQL construction.'), bullet('Internal exception details are logged instead of being displayed to end users.'), bullet('The Flask secret key is stored in local configuration or an environment variable.'), bullet('The application avoids collecting unnecessary personal information.'),
          P('The system intentionally does not include advanced enterprise features such as OAuth, JWT, API gateways, distributed infrastructure, or automatic threat monitoring. The goal is to demonstrate good foundational practice: controlled user access, validated data, safe database interaction, and readable error messages.'),
          P('6.3 Logging','H2x'),
          P('Python logging records application startup, login success or failure, task creation and deletion, prediction generation, CSV processing, and unexpected errors. Logs help a developer diagnose problems without exposing technical details to normal users.'), PageBreak()]
#8
story += [P('7. User Interface and Batch Prediction','H1x'),
          P('The interface is designed to make the prediction workflow clear for users who may not have technical knowledge of machine learning. Pages use familiar web patterns: forms for data entry, tables for task lists, status labels, filters, and simple visual summaries.'),
          tbl([['Page','Main elements and user outcome'],['Login and Register','Name, email, password fields and clear feedback for invalid credentials.'],['Dashboard','Total tasks, count by priority, overdue count, recent tasks, and a bar chart.'],['Task List','Task name, deadline, score, priority, status, search, filters, edit and delete actions.'],['Task Form','Required task fields, server-side validation, prediction result, explanation messages, and override option.'],['Task Detail','Full task record, saved prediction, model output, priority score, and override history.'],['Batch Prediction','CSV upload, invalid-row messages, result preview, and download action.']], [1.55*inch,4.75*inch]),
          P('7.1 Batch Prediction Workflow','H2x'),
          P('Batch processing enables a user to evaluate many tasks at once. The user uploads a CSV file with the required columns. The application checks column names and validates individual rows before calling the same scoring and prediction logic used for a single task. Invalid rows are reported with simple messages instead of silently failing. Valid rows receive a priority score and label, and the user can download the result as a CSV file. The initial version is limited to roughly 500 tasks per upload, which is suitable for a local internship demonstration.'),
          P('7.2 Manual Override','H2x'),
          P('A recommendation should support human judgement, not remove it. After viewing the predicted category, a user may select a different priority. The system requires a reason for the change and saves the original prediction, selected priority, reason, and time of the override. This provides an audit trail and makes the application more practical in real work situations where a manager may know context that is not captured by the task fields.'),
          P('The dashboard remains simple: it summarizes the amount of work by priority and highlights overdue tasks. These views help users identify workload patterns while avoiding the complexity of enterprise analytics platforms.'), PageBreak()]
#9
story += [P('8. Testing, Risks and Validation','H1x'),
          P('Testing verifies that the application behaves correctly for normal actions as well as invalid input. Pytest supports unit tests for isolated functions and integration tests for complete user workflows. The test suite should be run whenever changes are made to scoring, validation, database operations, or routes.'),
          tbl([['Testing Area','Example checks'],['Priority score','Low, medium, high, overdue, quick-win and dependency-heavy cases produce expected scores.'],['Validation','Invalid impact, urgency, effort, deadline and missing fields are rejected.'],['Feature preparation','Days-to-deadline and task-type encoding match the training format.'],['Prediction','The model returns only Low, Medium, High, or Critical.'],['Database CRUD','Tasks can be created, read, updated, and deleted correctly.'],['Integration','Login -> task creation -> prediction -> database save; CSV upload -> result download.']], [1.7*inch,4.6*inch]),
          P('8.1 Acceptance Criteria','H2x'),
          P('The project is accepted when the application starts locally, a user can register and sign in, task operations work correctly, invalid inputs are rejected, valid tasks receive a score from 0 to 100 and one of four labels, prediction details are saved, manual overrides include a reason, CSV batch prediction produces downloadable results, and the dashboard shows basic counts and a priority chart. Automated tests should cover core functionality and the model should reach a reasonable initial accuracy target on test data.'),
          P('8.2 Risks and Mitigation','H2x'),
          tbl([['Risk','Mitigation'],['Small or imbalanced dataset','Generate more realistic task examples and review the number of examples in each class.'],['Poor model accuracy','Clean data, verify features, and tune simple Decision Tree settings.'],['Incorrect input','Validate fields before calculation and prediction.'],['Wrong suggestion','Show score and reasons; allow a manual override with a saved reason.'],['Invalid CSV format','Check required columns and identify row-level errors.'],['Missing model file','Show a clear service error and document the training step.']], [2.15*inch,4.15*inch]),
          P('Testing and risk management reinforce the same principle: the recommendation is only useful when it is understandable, traceable, and dependable for common user actions.'), PageBreak()]
#10
story += [P('9. Implementation Plan, Conclusion and Future Work','H1x'),
          P('The project can be implemented incrementally. First, the Flask structure and basic pages are created. Next, the SQLite database and task CRUD operations are implemented. Validation and scoring logic are added before preparing the dataset and training the Decision Tree model. The saved model is then connected to the application. Dashboard charts, CSV processing, tests, documentation, and a local demonstration complete the work.'),
          tbl([['Phase','Main outcome'],['1 to 3','Flask project setup, database tables and task CRUD operations.'],['4 to 6','Validation rules, dataset preparation and priority scoring module.'],['7 to 8','Decision Tree training and saved-model integration.'],['9 to 10','Dashboard chart and CSV batch prediction.'],['11 to 12','Pytest coverage, defect fixes, documentation and final demonstration.']], [1.45*inch,4.85*inch]),
          P('9.1 Technology Stack','H2x'),
          tbl([['Layer','Technology','Purpose'],['Application','Python and Flask','Core logic, routes, forms, sessions and templates.'],['Data and ML','Pandas, NumPy, Scikit-learn and Joblib','Data preparation, Decision Tree model and persistence.'],['Storage and interface','SQLite, HTML, CSS, Bootstrap and Matplotlib','Local storage, responsive pages and dashboard charts.'],['Testing','Pytest','Unit and integration testing.']], [1.35*inch,2.1*inch,2.85*inch]),
          P('9.2 Conclusion','H2x'),
          P('Smart Task Priority Predictor turns task information into an understandable priority recommendation. It combines task management, a transparent score, a basic machine learning classifier, readable explanations, and manual user control. The design is practical for an intermediate internship project because each layer can be built and tested locally using familiar Python tools. It demonstrates frontend development, Flask routing, SQLite CRUD operations, data preprocessing, basic classification, error handling, testing, and documentation in one coherent project.'),
          P('9.3 Future Enhancements','H2x'),
          P('Future versions may use a larger real-world dataset, compare a Random Forest model, add project-level grouping and filters, introduce notifications, collect feedback on recommendations, and deploy to a simple hosting environment. Advanced AI, automatic retraining, real-time monitoring, and external project-management integrations remain outside the scope of this version.'),
          Spacer(1,0.12*inch), P('Prepared from the Software Requirements Specification for Smart Task Priority Predictor.','Cap')]

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=48,bottomMargin=52,title='Smart Task Priority Predictor Project Report',author='SANJAY S')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT.resolve())

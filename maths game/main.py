import pgzrun
WIDTH=870
HEIGHT=650
TITLE="maths game"
M_message=""
q_file_name="question.txt"
question_count=0
question_index=0
questions=[]
score=0
message=""
game_state=False
time_left=10

m_box=Rect(0,0,880,80)
q_box=Rect(0,0,650,150)
timer_box=Rect(0,0,150,150)
answer_box1=Rect(0,0,300,150)
answer_box2=Rect(0,0,300,150)
answer_box3=Rect(0,0,300,150)
answer_box4=Rect(0,0,300,150)
answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
skip_box=Rect(0,0,150,330)

m_box.move_ip(0,0)
q_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    screen.blit("cute",(0,0))
    global M_message
    screen.draw.filled_rect(m_box,"medium violet red")
    screen.draw.filled_rect(q_box,"navy blue")
    screen.draw.filled_rect(timer_box,"maroon")
    screen.draw.filled_rect(skip_box,"purple")
    for box in answer_boxes:
        screen.draw.filled_rect(box,"indigo")
    M_message="Welcome to quiz master..."
    screen.draw.textbox(M_message,m_box,color="hot pink")
    screen.draw.textbox("skip",skip_box,color="pink")
    screen.draw.textbox(str(time_left),timer_box,color="white")
    screen.draw.textbox(question[0].strip(),q_box,color="white")
    index=1
    for box in answer_boxes:
        screen.draw.textbox(question[index].strip(),box,color="black")
        index=index+1
 
def update():
    move_message()

def move_message():
    m_box.x=m_box.x-2
    if m_box.right<0:
        m_box.left=WIDTH

def read_question_fill():
    global question_count,questions
    q_file=open(q_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_question():
    global question_index,questions
    question_index=question_index+1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index=1
    for d in answer_boxes:
        if d.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index=index+1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score,question,questions,time_left
    score=score+1
    if questions:
        question=read_next_question()
        time_left=10
    else:
        game_over()

def game_over():
    global question,game_state,score,time_left
    message=f"game over!\n you got {score} question correct"
    question=[message,"-","-","-","-",5]
    time_left=0
    game_state=True

def skip_question():
    global question,time_left
    if questions and not game_state:
        question=read_next_question()
        time_left=10
    else:
        game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        game_over()

read_question_fill()
question=read_next_question()
clock.schedule_interval(update_time_left,1)
pgzrun.go()
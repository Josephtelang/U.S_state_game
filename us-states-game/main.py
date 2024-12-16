import turtle
import pandas


screen =turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput(title="Guess the State", prompt= "what's another state's name?").lower()
# print(answer_state )

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()


# correct_answer = 0
# game_over = False
# while game_over == False :
#     answer_state = screen.textinput(title=f"{correct_answer}/50 states correct" ,prompt= "what's another state's name?").capitalize()
       
#     if answer_state == "Exit":
#         game_over = True
        
#     if answer_state in all_states:
#         correct_answer += 1
#         state_data = data[data["state"] == answer_state]
#         print(state_data)
#         corrdinate_ans_state = state_data["x"].iloc[0],state_data["y"].iloc[0]
#         print(corrdinate_ans_state)
#         tim = turtle.Turtle()
#         tim.penup()
#         tim.hideturtle()
#         tim.goto(corrdinate_ans_state)
#         tim.write(answer_state)

            #oR

gussed_states = []    
while len(gussed_states) <= 50 :
    answer_state = screen.textinput(title=f"{len(gussed_states)}/50 states correct",prompt="what's another states name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in gussed_states:
                missing_states.append(state)
        print(missing_states)
        break
    
    if answer_state in all_states :
        gussed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        corrdinate_of_state =  state_data.x.item(),state_data.y.item()
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(corrdinate_of_state)
        tim.write(state_data.state.item())
        
# states_to_learn.csv


state_to_learn = pandas.DataFrame(missing_states)
state_to_learn.to_csv("states_to_learn.csv")


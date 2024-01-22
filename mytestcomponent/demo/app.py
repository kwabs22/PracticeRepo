
import gradio as gr
from gradio_mytestcomponent import MyTestComponent


example = MyTestComponent().example_inputs()

demo = gr.Interface(
    lambda x:x,
    MyTestComponent(),  # interactive version of your component
    MyTestComponent(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()

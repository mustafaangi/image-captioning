import gradio as gr

def greet(name):
    """
    Generate a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(server_name="localhost", server_port=7861)


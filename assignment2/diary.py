# Task 1: Diary
# This program appends user diary entries to diary.txt.
# It keeps asking for input until the user enters "done for now".

import traceback

try:
    # Open diary.txt in append mode.
    # The with statement closes the file automatically.
    with open("diary.txt", "a", encoding="utf-8") as diary_file:

        first_prompt = True

        while True:
            if first_prompt:
                entry = input("What happened today? ")
                first_prompt = False
            else:
                entry = input("What else? ")

            # Write every entry, including "done for now".
            diary_file.write(entry + "\n")

            if entry == "done for now":
                break

except Exception as e:
    print("An exception occurred.")

    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []

    for trace in trace_back:
        stack_trace.append(
            f"File: {trace[0]}, Line: {trace[1]}, "
            f"Func.Name: {trace[2]}, Message: {trace[3]}"
        )

    print(f"Exception type: {type(e).__name__}")

    message = str(e)
    if message:
        print(f"Exception message: {message}")

    print(f"Stack trace: {stack_trace}")
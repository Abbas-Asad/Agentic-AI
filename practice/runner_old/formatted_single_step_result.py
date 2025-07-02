# SingleStepResult(
#     original_input="What's is right angle? You can also handoff.",
#     model_response=ModelResponse(
#         output=[
#             ResponseOutputMessage(
#                 id='__fake_id__',
#                 content=[
#                     ResponseOutputText(
#                         annotations=[],
#                         text='A right angle is an angle that measures exactly 90 degrees. It is often represented by a small square drawn in the corner where the two lines forming the angle meet.  You can think of it as a perfect "L" shape.\n',
#                         type='output_text',
#                         logprobs=None
#                     )
#                 ],
#                 role='assistant',
#                 status='completed',
#                 type='message'
#             )
#         ],
#         usage=Usage(
#             requests=1,
#             input_tokens=40,
#             input_tokens_details=InputTokensDetails(cached_tokens=0),
#             output_tokens=50,
#             output_tokens_details=OutputTokensDetails(reasoning_tokens=0),
#             total_tokens=90
#         ),
#         response_id=None
#     ),
#     pre_step_items=[
#         HandoffCallItem(
#             agent=Agent(name='Assistant', ...),  # Agent details hidden for readability
#             raw_item=ResponseFunctionToolCall(arguments='{}', call_id='', name='transfer_to_math_expert', type='function_call', id='__fake_id__', status=None),
#             type='handoff_call_item'
#         ),
#         HandoffOutputItem(
#             agent=Agent(name='Assistant', ...), # Agent details hidden for readability
#             raw_item={'call_id': '', 'output': "{'assistant': 'Math expert'}", 'type': 'function_call_output'},
#             source_agent=Agent(name='Assistant', ...), # Agent details hidden for readability
#             target_agent=Agent(name='Math expert', ...), # Agent details hidden for readability
#             type='handoff_output_item'
#         )
#     ],
#     new_step_items=[
#         MessageOutputItem(
#             agent=Agent(name='Math expert', ...), # Agent details hidden for readability
#             raw_item=ResponseOutputMessage(
#                 id='__fake_id__',
#                 content=[
#                     ResponseOutputText(
#                         annotations=[],
#                         text='A right angle is an angle that measures exactly 90 degrees. It is often represented by a small square drawn in the corner where the two lines forming the angle meet.  You can think of it as a perfect "L" shape.\n',
#                         type='output_text',
#                         logprobs=None
#                     )
#                 ],
#                 role='assistant',
#                 status='completed',
#                 type='message'
#             ),
#             type='message_output_item'
#         )
#     ],
#     next_step=NextStepFinalOutput(
#         output='A right angle is an angle that measures exactly 90 degrees. It is often represented by a small square drawn in the corner where the two lines forming the angle meet.  You can think of it as a perfect "L" shape.\n'
#     )
# ) 
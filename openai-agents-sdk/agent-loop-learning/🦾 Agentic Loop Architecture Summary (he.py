🦾 Agentic Loop Architecture Summary (heading)

Runner.run(
    setup:
        tool_use_tracker
        context_wrapper
        generated_items = []
        model_responses = []
        input_guardrail_results = []
        current_agent = starting_agent
        current_turn = 0
        current_span = None  # for tracing

    while True:  # Agent loop starts
        # 1️⃣ Tracing setup for agent
        if current_span is None:
            current_span = agent_span(current_agent)

        # 2️⃣ Check turn limit
        if current_turn > max_turns:
            raise MaxTurnsExceeded

        # 3️⃣ First turn => Run input guardrails + single_turn in parallel
        if turn == 1:
            input_guardrail_results, turn_result = await asyncio.gather(
                _run_input_guardrails(...),
                _run_single_turn(...)
            )
        else:
            turn_result = await _run_single_turn(...)

        # 4️⃣ Save response + prepare for next step
        model_responses.append(turn_result.model_response)
        original_input = turn_result.original_input
        generated_items = turn_result.generated_items

        # 5️⃣ Handle next step
        if FinalOutput:
            run output guardrails
            return RunResult(...)
        
        elif NextStepHandoff:
            switch current_agent => new_agent
            reset current_span
        
        elif NextStepRunAgain:
            continue

        else:
            raise AgentsException("Unknown next step type")

🔁 _run_single_turn() — Mini Agent Turn (heading)

_run_single_turn(
    if first turn: run hooks.on_start()

    get system_prompt
    output_schema = get_output_schema(agent)
    handoffs = get_handoffs(agent)

    input = original_input + previous_generated_items

    get new_response = _get_new_response(...)  # Model call

    return _get_single_step_result_from_response(...)
)
🤖 _get_new_response() — LLM Call (heading)

_get_new_response(
    model = resolve(agent.model, run_config.model)
    model_settings = merge(agent_settings, run_config_settings)
    model_settings = maybe_reset_tool_choice(...)

    return await model.get_response(...)  # Final LLM call
)
🧩 _get_single_step_result_from_response() — Process + Execute (heading)

_get_single_step_result_from_response(
    process_response = RunImpl.process_model_response(...)  # categorize model response

    tool_use_tracker.add_tool_use()

    return await RunImpl.execute_tools_and_side_effects(...)
)

🛡️ Guardrails Flow (heading)
Input Guardrails only run on the first turn:


_run_input_guardrails(
    for each guardrail:
        if tripwire: raise InputGuardrailTripwireTriggered
)
Output Guardrails only run on final output:


_run_output_guardrails(
    for each guardrail:
        if tripwire: raise OutputGuardrailTripwireTriggered
)










🧠 Tip to Remember Agent Loop Flow

🚦 Setup
🔁 Loop (one turn at a time)
    🎯 Call Agent → get system_prompt, handoffs
    📤 Prepare input → call model
    🧠 Analyze response → tool use / handoff / final output?
🛑 Stop when final output or max_turns
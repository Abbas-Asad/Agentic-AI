from agents import Agent, Runner
from agentsdk_gemini_adapter import config

agent = Agent(name="Assistant", instructions="You are a helpful assistant.")

# input = "Aaj mausam bohat... Log kya soch rahe hain? Kuch logon ki raaye likho."

input = "What is a machine?"

result = Runner.run_sync(agent, input, run_config=config)
print("\n")
print(result.final_output)







# Yani:
# Jab jawab ke options kam hain, temperature style ya wording badalta hai.
# Jab options zyada hain, temperature content bhi badal sakta hai.

# Aapka samajhna sahi hai, bas yeh yaad rakhein:
# temperature style ke sath sath kabhi kabhi content bhi badal sakta hai (agar options zyada ho).
# top_p pool ko limit karta hai, temperature us pool mein se pick karne ki randomness.
# Agar ab bhi koi confusion hai, ya aur example chahiye, toh zaroor poochein!

# top_p = 0.3:
# Sirf pehle 3 jawab consider honge (kyunki 0.30 + 0.20 + 0.10 = 0.60, lekin top_p pool cumulative probability se banta hai, lekin simple socho: top answers ka pool chhota ho gaya).
# temperature = 1.0:
# In 3 answers mein se koi bhi pick ho sakta hai, random style mein.
# temperature = 0.0:
# In 3 answers mein se sabse pehla (sabse zyada likely) hamesha pick hoga.





# -----------------notes-----------------
# Ek Line mein:
# top_p: Pool banata hai (kaunse jawab consider honge)
# temperature: Pool ke andar se pick karne ki randomness

# frequency_penalty: to mtlb frequency_penalty dekhta hain kay konsay words aaye hain phir un ko repeat krne se bchta hai jini zyada penalty ho # basically (probabiltity - penalty) calculation lgata hai  # blke sab hi apne piche calculation lgaty hongy

# max_tokens: max_output_tokens    (developer kay kam ki cheez lekin bech may output kaat deta hai

# tool_choice: required(tool use laazmi krna hai)  |  none(kabhi nhi krna)  |  auto(mrzi hai, jo tum chaho)  |  (If you provide specific tool name e.g. my_tool, it requires the LLM to use that specific tool.)      
# note: Literal["auto", "required", "none"] | str | None

# parallel_tool_calls: jitnay tool call ki zarurat hai sab ko ek sath call krna agr true hai wrna aik aik krke
# shayad await asyncio.gather(...)   (actually LLM sary ResponseFunctionToolCall aik sath hi de dega)
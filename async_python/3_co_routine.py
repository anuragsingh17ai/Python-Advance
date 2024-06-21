import asyncio

#create and acess   
loop = asyncio.new_event_loop()

#define a task
task1 = asyncio.sleep(2)

#execute  a task
loop.run_until_complete(task1)
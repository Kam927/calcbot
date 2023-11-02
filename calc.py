import discord
import math
from sympy import sympify, SympifyError
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="List of commands are:", color=discord.Color.blue())

    embed.add_field(name="!add", value="Adds two numbers: # # or # + #", inline=False)
    embed.add_field(name="!sub", value="Subtracts two numbers: # # or # - #", inline=False)
    embed.add_field(name="!div", value="Divides numbers: # # or # / #", inline=False)
    embed.add_field(name="!mul", value="Multiplies two numbers: # # or # * #", inline=False)
    embed.add_field(name="!cal", value="Calculates multiple operands and operators", inline=False)
    embed.add_field(name="!fac", value="Calculates Factorial: #", inline=False)
    embed.add_field(name="!pow", value="Calculates number to a power: # # or # ^ #", inline=False)
    embed.add_field(name="!btod", value="Binary to decimal", inline=False)
    embed.add_field(name="!dtob", value="Decimal to binary", inline=False)
    embed.add_field(name="!ftoc", value="Fahrenheit to Celsius", inline=False)
    embed.add_field(name="!ctof", value="Celsius to Fahrenheit", inline=False)

    await ctx.send(embed=embed)

#Adds only two numbers
@bot.command()
async def add(ctx, *args):
    try:
        #format  is # #
        if len(args) == 2:
            num1, num2 = int(args[0]), int(args[1])
        #format is # + #
        elif len(args) == 3 and args[1] == '+':
            num1, num2 = int(args[0]), int(args[2])

        result = num1 + num2
        await ctx.send(f"{num1} + {num2} = {result}")

    except ValueError:
        await ctx.send("Invalid format")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

#Subs only two numbers
@bot.command()
async def sub(ctx, *args):
    try:
        #format  is # #
        if len(args) == 2:
            num1, num2 = int(args[0]), int(args[1])
        #format is # - #
        elif len(args) == 3 and args[1] == '-':
            num1, num2 = int(args[0]), int(args[2])

        result = num1 - num2
        await ctx.send(f"{num1} - {num2} = {result}")

    except ValueError:
        await ctx.send("Invalid format")

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

#Divs only two numbers
@bot.command()
async def div(ctx, *args):
    try:
        #format  is # #
        if len(args) == 2:
            num1, num2 = int(args[0]), int(args[1])
        #format is # / #
        elif len(args) == 3 and args[1] == '/':
            num1, num2 = int(args[0]), int(args[2])

        result = num1 / num2
        await ctx.send(f"{num1} / {num2} = {result}")
    except ValueError:
        await ctx.send("Invalid format")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def mul(ctx, *args):
    try:
        #format  is # #
        if len(args) == 2:
            num1, num2 = int(args[0]), int(args[1])
        #format is # * #
        elif len(args) == 3 and args[1] == '*':
            num1, num2 = int(args[0]), int(args[2])
        else:
            raise ValueError("Invalid format")

        result = num1 * num2
        await ctx.send(f"{num1} * {num2} = {result}")
    except ValueError as e:
        await ctx.send(str(e))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

#Accepts multiple operands and operators
@bot.command()
async def calculate(ctx, *, equation: str):
    try:
        #Use SymPy to evaluate the equation
        result = sympify(equation)
        await ctx.send(f"Result: {result}")
    except SympifyError:
        await ctx.send("Invalid mathmatical expression!")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

#Power
@bot.command()
async def pow(ctx, *args):
    try:
        #format  is # #
        if len(args) == 2:
            num, exp = int(args[0]), int(args[1])
        #format is # ^ #
        elif len(args) == 3 and args[1] == '^':
            num, exp = int(args[0]), int(args[2])
        result = 1
        for i in range(exp):
            result *= num
        await ctx.send(f"{num}^{exp} = {result}")

    except ValueError:
        await ctx.send("Invalid format")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")


#Factorial
@bot.command()
async def fac(ctx, *args):
    try:
        #format is # 
        if len(args) == 1:
            fac = int(args[0]) 
        result = math.factorial(fac)
        await ctx.send(f"!{fac} = {result}")
    except ValueError:
        await ctx.send("Invalid format")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# to binary
@bot.command()
async def dtob(ctx, num_str: str):
    try:
        #check if valid number
        if not num_str.isnumeric(): 
            raise ValueError("Invalid format")

        dec = int(num_str)
        #not bigger than 4 bytes or negative
        if dec < 0 or dec > 4294967295:
            raise ValueError("Number is out of range.")

        result = bin(dec)

        await ctx.send(f" Decimal {num_str} = Binary {result}")
    except ValueError as e:
        await ctx.send(str(e))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# to decimal 
@bot.command()
async def btod(ctx, bin_str: str):
    try:
        #check string format to be only 1s and 0s
        if not all(char in ['0', '1'] for char in bin_str):
            raise ValueError("Invalid format")
        #convert it
        result = int(bin_str, 2)
        
        await ctx.send(f" Binary {bin_str} = Decimal {result}")
    except ValueError as e:
        await ctx.send(str(e))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

#Farhenheit to Celsius
@bot.command()
async def ftoc(ctx, f: str):
    try:
        f = float(f)
        result = (f - 32) * (5/9)

        await ctx.send(f"{f}°F --> {result:.2f}°C.")
    except ValueError:
        await ctx.send("Invalid Format")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Celsius to Farhenheit
@bot.command()
async def ctof(ctx, c: str):
    try:
        c = float(c)
        result = c * 9/5 + 32

        await ctx.send(f"{c}°C --> {result:.2f}°F.")
    except ValueError:
        await ctx.send("Invalid Format")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")





# M
bot.run("TE2NTM0MjEyNDY3MDIwNjA0NA.GF6cdK.D0c-Ipw2bQdDHzeUUB3q8rRvY12V0ovEuFjYNo")

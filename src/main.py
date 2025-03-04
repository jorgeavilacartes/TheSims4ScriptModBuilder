import services
import sims4.commands
from protocolbuffers import Consts_pb2

@sims4.commands.Command('hello', command_type=sims4.commands.CommandType.Live)
def hello_world(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("Hello World")


@sims4.commands.Command('cheats_help', command_type=sims4.commands.CommandType.Live)
def hello_world(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("add_money <amount>: add money to your current sim")
    output("remove_money <amount>: remove money from your current sim")
    output("max_skill <skill name (no space)>: set the skill to max level")
    output("become_friend <firstname> <lastname>: become friend with the target sim")
    output("become_lover <firstname> <lastname>: become lover with the target sim")


@sims4.commands.Command('motherlode_plus', command_type=(sims4.commands.CommandType.Live),
                        console_type=(sims4.commands.CommandType.Cheat))
def motherlode_plus(amount: int = 0, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    modify_fund_helper(amount, Consts_pb2.TELEMETRY_MONEY_CHEAT, tgt_client.active_sim)

def modify_fund_helper(amount, reason, sim):
    if amount > 0:
        sim.family_funds.add(amount, reason, sim)
    else:
        sim.family_funds.try_remove(-amount, reason, sim)
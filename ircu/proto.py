from ircu.p10 import endofburst as p10_endofburst
from ircu.p10 import endofburst_ack as p10_endofburst_ack
from ircu.p10 import nick as p10_nick
from ircu.p10 import passw as p10_pass
from ircu.p10 import ping as p10_ping
from ircu.p10 import server as p10_server


HANDLERS = {
    ('PASS', 'PA'): p10_pass.MessageHandler,
    ('PING', 'G'): p10_ping.MessageHandler,
    ('SERVER', 'S'): p10_server.MessageHandler,
    ('NICK', 'N'): p10_nick.MessageHandler,
    ('END_OF_BURST', 'EB'): p10_endofburst.MessageHandler,
    ('END_OF_BURST_ACK', 'EA'): p10_endofburst_ack.MessageHandler,
}


def handler_lookup(token):
    for (hnd_token, hnd_cmd) in HANDLERS:
        if hnd_token == token or hnd_cmd == token:
            return HANDLERS[(hnd_token, hnd_cmd)]
    return None

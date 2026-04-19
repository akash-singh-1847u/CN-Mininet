from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

packet_count = {}
THRESHOLD = 20

def _handle_PacketIn(event):
    packet = event.parsed
    src = str(packet.src)

    packet_count[src] = packet_count.get(src, 0) + 1
    log.info(f"{src} -> {packet_count[src]}")

    if packet_count[src] > THRESHOLD:
        log.info(f"BLOCKING {src}")

        block = of.ofp_flow_mod()
        block.match.dl_src = packet.src
        block.actions = []  # DROP
        event.connection.send(block)
        return   # IMPORTANT: stop forwarding

    # normal forwarding
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)
def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

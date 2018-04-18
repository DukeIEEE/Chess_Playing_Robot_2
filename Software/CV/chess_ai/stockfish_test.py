import chess
import chess.uci
import sys

engine = chess.uci.popen_engine("stockfish_8_x64.exe")
engine.uci()
print(engine.name)
# board = chess.Board("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1")
#board = chess.Board("8/8/5P2/2q5/5K2/2p5/k7/7Q w - - 80 151")
board = chess.Board()

print(sys.version)
for x in range(20):
    engine.position(board)
    (bestmove, ponder) = engine.go(movetime=100)
    board.push(bestmove)
    print(board)
    print(board.fen())

# print(board.is_stalemate())
# print(board.is_insufficient_material())
# print(board.is_game_over())
# print(board.can_claim_threefold_repetition())
# print(board.can_claim_fifty_moves())
# print(board.can_claim_draw())
# print(board.is_fivefold_repetition())
# print(board.is_seventyfive_moves())
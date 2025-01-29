emoji_map = {
  "happy": ":beaming_face_with_smiling_eyes:",
  "sad": ":frowning_face:",
  "angry": ":angry_face:",
  "neutral": ":neutral_face:",
  "surprise": ":astonished_face:"
}
import emoji


def emojize(pred_class):
    emote = emoji_map[pred_class]
    emote = emoji.emojize(emote)
    print(emote)
    return emote
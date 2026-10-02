#Hẹn hò nhưng không yêu 
#Mọi người sài nhớ cre nha !! 
#code by Tranchinnn
#code mang tính chia sẻ giải trí không toxic
import sys
import os
import time
import threading

def play_music(filename="music.mp3"):
    """
    Phát nhạc nền liên tục bằng pygame.
    Nếu pygame chưa cài,sẽ tự động cài nhé.
    """
    import contextlib, io

    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            import pygame
    except ImportError:
        try:
            import subprocess
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
                import pygame
        except Exception:
            return  

    if not os.path.exists(filename):
        return

    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play(-1)  
    except Exception:
        return


class Mau:
    RESET = '\033[0m'
    TRANG = (255, 255, 255)
    DEN = (50, 50, 50)

def xoa_man_hinh():
    """Xóa màn hình terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')



def hieu_ung_tung_tu_ro_dan(line, char_speed=0.08, word_delay=0.3, fade_steps=6):
    words = line.split()
    displayed_line = ""

    for word in words:
        for step in range(1, fade_steps + 1):
            intensity = int(Mau.TRANG[0] * (fade_steps - step + 1) / fade_steps)
            temp_line = displayed_line + f"\033[38;2;{intensity};{intensity};{intensity}m{word}{Mau.RESET} "
            sys.stdout.write(f"\r{temp_line}")
            sys.stdout.flush()
            time.sleep(char_speed)
        displayed_line += f"\033[38;2;{Mau.TRANG[0]};{Mau.TRANG[1]};{Mau.TRANG[2]}m{word}{Mau.RESET} "
        sys.stdout.write(f"\r{displayed_line}")
        sys.stdout.flush()
        time.sleep(word_delay)

    print()
    return displayed_line

def hieu_ung_go_chu(line, char_speed=0.05):
    current_line = ""
    for char in line:
        current_line += f"\033[38;2;{Mau.TRANG[0]};{Mau.TRANG[1]};{Mau.TRANG[2]}m{char}{Mau.RESET}"
        sys.stdout.write(f"\r{current_line}")
        sys.stdout.flush()
        time.sleep(char_speed)
    print()
    return current_line
def hieu_ung_laser(line, step_delay=0.03, laser_width=3):
    length = len(line)
    for pos in range(length + laser_width):
        temp_line = ""
        for i, c in enumerate(line):
            if pos - laser_width <= i <= pos:
                temp_line += f"\033[38;2;{Mau.TRANG[0]};{Mau.TRANG[1]};{Mau.TRANG[2]}m{c}{Mau.RESET}"
            else:
                temp_line += f"\033[38;2;{Mau.DEN[0]};{Mau.DEN[1]};{Mau.DEN[2]}m{c}{Mau.RESET}"
        sys.stdout.write(f"\r{temp_line}")
        sys.stdout.flush()
        time.sleep(step_delay)
    gray_value = 180
    final_line = f"\033[38;2;{gray_value};{gray_value};{gray_value}m{line}{Mau.RESET}"
    sys.stdout.write(f"\r{final_line}\n")
    sys.stdout.flush()
    return line

def show_lyrics():
    lyrics_list = [
        "Con tốt mang tên em mà anh lựa chọn bước đi.",
        "Hẹn hò nhưng không yêu, chắc em là kẻ mất trí",
        "Hẹn hò nhưng không yêu, thế yêu định nghĩa là gì?",
        "Chạy về người ngàn bước cớ sao người lại từ khước",
        "Một bước quay lại về phía em.",
        "Em cố trăm lần ",
        "chẳng bằng ai đó 1 phần",
        "Em cố trăm lần ",
        "chẳng bằng ai đó 1 phần",
        "Những khi anh nói anh cần.. ở đâu em cũng chạy đến bên anh.",
        "Mưa gió không ngại, chỉ ngại anh ở bên ai, rồi em phải cố nén lại từng cơn nhói đau trong lòng"
    ]

    char_speed_list = [0.08, 0.07, 0.07, 0.07, 0.06, 0.01, 0.01, 0.01, 0.01, 0.056, 0.067]
    effect_order    = [2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 2] # các hiệu ứng từ (0,1,2)

    xoa_man_hinh()
    for idx, line in enumerate(lyrics_list):
        effect_type = effect_order[idx]
        speed = char_speed_list[idx]
        if effect_type == 0:
            hieu_ung_tung_tu_ro_dan(line, char_speed=speed)
        elif effect_type == 1:
            hieu_ung_go_chu(line, char_speed=speed)
        else:
            hieu_ung_laser(line, step_delay=speed)

    time.sleep(0.5)


if __name__ == "__main__":
    music_thread = threading.Thread(target=play_music, args=("music.mp3",), daemon=True)
    music_thread.start()
    show_lyrics()

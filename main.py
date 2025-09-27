import cv2
import os
import time

# --- 1. 参数设置 ---
# 输入视频文件名
INPUT_VIDEO_PATH = 'input.mp4'

# 保存帧的文件夹名称
OUTPUT_FOLDER = 'video_frames'

# 字符集，用于构成字符画
ASCII_CHARS = "@%#*+=-:. "

# 每一帧字符画的宽度（字符数）
ASCII_WIDTH = 100

# --- 2. 核心功能函数 ---

def clear_console():
    """清空控制台"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ascii_char(gray_value):
    """根据灰度值返回对应的ASCII字符"""
    index = int(gray_value * len(ASCII_CHARS) / 256)
    return ASCII_CHARS[min(index, len(ASCII_CHARS) - 1)]

def frame_to_ascii(frame):
    """将一帧视频图像转换为ASCII字符字符串"""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray_frame.shape
    ascii_height = int(ASCII_WIDTH * height / width * 0.5)
    resized_gray_frame = cv2.resize(gray_frame, (ASCII_WIDTH, ascii_height))
    
    ascii_str = ""
    for i in range(ascii_height):
        for j in range(ASCII_WIDTH):
            pixel_gray = resized_gray_frame[i, j]
            ascii_str += get_ascii_char(pixel_gray)
        ascii_str += "\n"
    return ascii_str

def save_ascii_frame(ascii_string, frame_number, folder_name):
    """
    将ASCII字符串保存为文本文件
    :param ascii_string: 要保存的ASCII字符画
    :param frame_number: 帧的序号，用于文件名
    :param folder_name: 保存文件的文件夹
    """
    # 确保文件夹存在，如果不存在则创建
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # 构建完整的文件路径和名称，例如 'video_frames/1.txt'
    file_path = os.path.join(folder_name, f"{frame_number}.txt")
    
    # 打开文件并写入内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(ascii_string)

# --- 3. 主程序 ---

def main():
    if not os.path.exists(INPUT_VIDEO_PATH):
        print(f"错误：输入文件 '{INPUT_VIDEO_PATH}' 不存在！")
        return

    cap = cv2.VideoCapture(INPUT_VIDEO_PATH)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1.0 / fps

    print("ASCII视频即将开始播放，并同时保存帧到 'video_frames' 文件夹。")
    print("按 Ctrl+C 退出。")
    time.sleep(2)

    frame_count = 0 # 用于计数和命名文件

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame_count += 1 # 帧计数器加一

                # 1. 将当前帧转换为ASCII字符串
                ascii_frame = frame_to_ascii(frame)
                
                # 2. 清空控制台并打印ASCII帧
                clear_console()
                print(ascii_frame)
                print(f"正在播放第 {frame_count} 帧...") # 在底部显示当前帧数
                
                # 3. 保存ASCII字符串到文件
                save_ascii_frame(ascii_frame, frame_count, OUTPUT_FOLDER)
                
                # 4. 控制播放速度
                start_time = time.time()
                elapsed_time = time.time() - start_time
                sleep_time = max(0, frame_delay - elapsed_time)
                time.sleep(sleep_time)
            else:
                break # 视频播放完毕
    except KeyboardInterrupt:
        print("\n播放已停止。")
    finally:
        cap.release()
        print(f"\n播放结束！所有帧已保存到 '{OUTPUT_FOLDER}' 文件夹。")


if __name__ == '__main__':
    main()

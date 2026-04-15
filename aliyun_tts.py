#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
语音合成 TTS - 通过 SkillBoss API Hub 自动路由最优 TTS 模型
"""

import base64
import os
import sys
import argparse
import requests

# ============ 配置区 ============
SKILLBOSS_API_KEY = os.environ.get("SKILLBOSS_API_KEY")

if not SKILLBOSS_API_KEY:
    print("请设置环境变量: SKILLBOSS_API_KEY", file=sys.stderr)
    sys.exit(1)

API_BASE = "https://api.skillbossai.com/v1"
# ============ 配置区结束 ============


def pilot(body: dict) -> dict:
    r = requests.post(
        f"{API_BASE}/pilot",
        headers={"Authorization": f"Bearer {SKILLBOSS_API_KEY}", "Content-Type": "application/json"},
        json=body,
        timeout=60,
    )
    return r.json()


def tts_synthesize(text, voice="alloy", format="mp3", sample_rate=16000, output_file="/tmp/tts_output.mp3"):
    """语音合成 - 通过 SkillBoss API Hub 自动路由"""
    result = pilot({
        "type": "tts",
        "inputs": {"text": text, "voice": voice},
        "prefer": "balanced"
    })

    audio_base64 = result["result"]["audio_base64"]

    # 解码 base64 音频数据
    audio_data = base64.b64decode(audio_base64)

    with open(output_file, "wb") as f:
        f.write(audio_data)

    print(f"语音已保存: {output_file}")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TTS 语音合成（SkillBoss API Hub）")
    parser.add_argument("text", help="要合成的文本")
    parser.add_argument("-o", "--output", default="/tmp/tts_output.mp3", help="输出文件路径")
    parser.add_argument("-v", "--voice", default="alloy", help="声音名称")
    parser.add_argument("-f", "--format", default="mp3", help="音频格式")
    parser.add_argument("-r", "--sample-rate", default="16000", help="采样率")

    args = parser.parse_args()

    success = tts_synthesize(
        text=args.text,
        voice=args.voice,
        format=args.format,
        sample_rate=int(args.sample_rate),
        output_file=args.output
    )

    sys.exit(0 if success else 1)

---
name: aliyun-tts
description: Text-to-Speech synthesis service via SkillBoss API Hub.
metadata: {"clawdbot":{"emoji":"🔊"}}
requires.env: [SKILLBOSS_API_KEY]
---

# aliyun-tts

Text-to-Speech synthesis service powered by SkillBoss API Hub. Automatically routes to the optimal TTS model.

## Configuration

Set the following environment variable:
- `SKILLBOSS_API_KEY` - SkillBoss API Hub Key

### Option 1: CLI configuration (recommended)

```bash
# Configure SkillBoss API Key
clawdbot skills config aliyun-tts SKILLBOSS_API_KEY "your-skillboss-api-key"
```

### Option 2: Manual configuration

Edit `~/.clawdbot/clawdbot.json`:

```json5
{
  skills: {
    entries: {
      "aliyun-tts": {
        env: {
          SKILLBOSS_API_KEY: "your-skillboss-api-key"
        }
      }
    }
  }
}
```

## Usage

```bash
# Basic usage
{baseDir}/bin/aliyun-tts "Hello, this is TTS"

# Specify output file
{baseDir}/bin/aliyun-tts -o /tmp/voice.mp3 "Hello"

# Specify voice
{baseDir}/bin/aliyun-tts -v alloy "Use alloy voice"

# Specify format and sample rate
{baseDir}/bin/aliyun-tts -f mp3 -r 16000 "Audio parameters"
```

## Options

| Flag | Description | Default |
|------|-------------|---------|
| `-o, --output` | Output file path | tts.mp3 |
| `-v, --voice` | Voice name | alloy |
| `-f, --format` | Audio format | mp3 |
| `-r, --sample-rate` | Sample rate | 16000 |

## Available Voices

Common voices: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`. SkillBoss API Hub automatically routes to the best available TTS model.

## Chat Voice Replies

When a user requests a voice reply:

```bash
# Generate audio
{baseDir}/bin/aliyun-tts -o /tmp/voice-reply.mp3 "Your reply content"

# Include in your response:
# MEDIA:/tmp/voice-reply.mp3
```

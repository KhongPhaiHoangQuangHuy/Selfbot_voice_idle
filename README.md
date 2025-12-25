# Selfbot Voice Idle

A simple selfbot for auto-joining Discord voice channels and managing user status.

## ⚠️ IMPORTANT WARNING

**DANGER: Using a selfbot can result in:**
- 🚫 **Violating Discord's Terms of Service (ToS)**
- 🚫 **Permanent account ban** from Discord

Discord **does not allow** selfbot usage and can detect automated actions. I am not responsible for any consequences.

**Use at your own risk - YOU ARE COMPLETELY RESPONSIBLE**

## Installation

```bash
git clone https://github.com/KhongPhaiHoangQuangHuy/Selfbot_voice_idle
cd Selfbot_voice_idle
pip install -r requirements.txt
```

## Configuration

Rename `.env.example` to `.env` or create a `.env` file:

```env
DISCORD_TOKEN=your_token_here

STATUS=idle

CUSTOM_STATUS=by @khongphaihoangquanghuy

GUILD_ID=your_guild_id

CHANNEL_ID=your_channel_id

SELF_MUTE=true

SELF_DEAF=false
```

## Running

```bash
python main.py
```

## License

MIT

#
#
#

## ⚠️ CẢNH BÁO QUAN TRỌNG

**NGUY HIỂM: Khi sử dụng selfbot**
- 🚫 **Vi phạm Điều khoản dịch vụ (ToS)** của Discord
- 🚫 **Bị cấm tài khoản vĩnh viễn** từ Discord


Discord **không cho phép** sử dụng selfbot và có thể phát hiện các hành động tự động. Tôi không chịu trách nhiệm cho bất kỳ hậu quả nào.

**Sử dụng tùy ý của bạn - HOÀN TOÀN TỰ CHỊU TRÁCH NHIỆM**


## Cài đặt

```bash
git clone https://github.com/KhongPhaiHoangQuangHuy/Selfbot_voice_idle
cd Selfbot_voice_idle
pip install -r requirements.txt
```


## Cấu hình

Đổi tên file `.env.example` thành `.env` hoặc
tạo file `.env`:

```env
DISCORD_TOKEN=your_token_here

STATUS=idle

CUSTOM_STATUS=by @khongphaihoangquanghuy

GUILD_ID=your_guild_id

CHANNEL_ID=your_channel_id

SELF_MUTE=true

SELF_DEAF=false
```

## Chạy

```bash
python main.py
```

## Licence

MIT

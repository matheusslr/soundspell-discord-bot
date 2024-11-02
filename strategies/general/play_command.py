import discord
import yt_dlp

from strategies.base_command import CommandStrategy
from utils.decorators import command

@command("play")
class PlayCommand(CommandStrategy):
    def __init__(self):
        self.message = None

    async def execute(self, message: discord.Message, args: list[str]):
        self.message = message

        if message.author.voice:
            voice_channel = message.author.voice.channel
            if not message.guild.voice_client:
                await voice_channel.connect()
        else:
            await message.channel.send("Você precisa estar em um canal de voz para usar esse comando!")
            return

        if args[0].startswith("https://open.spotify.com/"):
            await self.play_spotify(args[0])
        elif args[0].startswith("https://www.youtube.com/") or args[0].startswith("https://youtu.be/"):
            await self.play_youtube(args[0])
        else:
            await message.channel.send("Por favor, forneça um link do YouTube ou Spotify válido.")

    async def play_youtube(self, query: str):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                url = info['url']

            voice_client = self.message.guild.voice_client
            if voice_client and voice_client.is_connected():
                voice_client.play(discord.FFmpegPCMAudio(url))
            else:
                await self.message.channel.send("Erro ao conectar ao canal de voz.")
        except yt_dlp.utils.DownloadError as e:
            await self.message.channel.send("Ocorreu um erro ao tentar extrair informações do vídeo.")
            print(f"Erro ao extrair vídeo: {e}")

    def play_spotify(self, query: str):
        pass

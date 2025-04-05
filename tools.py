from crewai_tools import YoutubeChannelSearchTool

def create_yt_tool(channel_handle):
    return YoutubeChannelSearchTool(youtube_channel_handle=channel_handle)
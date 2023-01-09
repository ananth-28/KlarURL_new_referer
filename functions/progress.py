import time
import math

from translation import Translation


async def progress_for_pyrogram(
        current,
        total,
        ud_type,
        message,
        start
):
    now = time.time()
    diff = now - start
    if (round(diff % 10.00) == 0 or current == total) and round(
        current / total * 100, 0
    ) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n".format(
            ''.join(
                [
                    Translation.DOWNLOAD_PROGRESS
                    for _ in range(math.floor(percentage / 5))
                ]
            ),
            ''.join(
                [
                    Translation.UPLOAD_PROGRESS
                    for _ in range(20 - math.floor(percentage / 5))
                ]
            ),
        )

        tmp = progress + Translation.PROGRESS.format(
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(text=f"**{ud_type}**\n\n {tmp}")
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: " ", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        n += 1
    return f"{str(round(size, 2))} {Dic_powerN[n]}B"


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)}g, " if days else "")
        + (f"{str(hours)}s, " if hours else "")
        + (f"{str(minutes)}d, " if minutes else "")
        + (f"{str(seconds)}s, " if seconds else "")
        + (f"{str(milliseconds)}ms, " if milliseconds else "")
    )
    return tmp[:-2]

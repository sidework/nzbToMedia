# coding=utf-8

import requests

from core.utils import shutil_custom
from core.utils.common import clean_dir, flatten, get_dirs, process_dir
from core.utils.download_info import get_download_info, update_download_info_status
from core.utils.encoding import char_replace, convert_to_ascii
from core.utils.files import (
    backup_versioned_file,
    extract_files,
    is_archive_file,
    is_media_file,
    is_min_size,
    list_media_files,
    move_file,
)
from core.utils.identification import category_search, find_imdbid
from core.utils.links import copy_link, replace_links
from core.utils.naming import clean_file_name, is_sample, sanitize_name
from core.utils.network import find_download, server_responding, test_connection, wake_on_lan, wake_up
from core.utils.notifications import plex_update
from core.utils.nzbs import get_nzoid, report_nzb
from core.utils.parsers import (
    parse_args,
    parse_deluge,
    parse_other,
    parse_qbittorrent,
    parse_rtorrent,
    parse_transmission,
    parse_utorrent,
    parse_vuze,
)
from core.utils.paths import (
    clean_directory,
    flatten_dir,
    get_dir_size,
    make_dir,
    onerror,
    rchmod,
    remote_dir,
    remove_dir,
    remove_empty_folders,
    remove_read_only,
)
from core.utils.processes import RunningProcess, restart
from core.utils.subtitles import import_subs
from core.utils.torrents import create_torrent_class, pause_torrent, remove_torrent, resume_torrent

requests.packages.urllib3.disable_warnings()
shutil_custom.monkey_patch()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MIME file type knowledge base."""

# list of known MIME types, apart from the ones starting with `text/`
# that can be safely rendered as textual data.
TEXT_MIME_TYPES = (
    'application/ecmascript',
    'application/javascript',
    'application/json',
    'application/typescript',
    'application/vnd.mozilla.xul+xml',
    'application/x-csh',
    'application/x-sh',
    'application/xhtml+xml',
    'application/xml',
)

HTML_MIME_TYPES = ('text/html', )

PDF_MIME_TYPES = ('application/pdf', )

ARCHIVE_MIME_TYPES = (
    'application/epub+zip',
    'application/zip',
    'application/x-tar',
    'application/x-rar-compressed',
    'application/gzip',
    'application/x-7z-compressed',
    'application/x-bzip2',
    'application/pdf',
    'application/x-msdownload',
    'application/x-shockwave-flash',
    'application/rtf',
    'application/x-nintendo-nes-rom',
    'application/x-google-chrome-extension',
    'application/vnd.ms-cab-compressed',
    'application/octet-stream',
    'application/postscript',
    'application/x-xz',
    'application/x-sqlite3',
    'application/x-deb',
    'application/x-unix-archive',
    'application/x-compress',
    'application/x-lzip',
)

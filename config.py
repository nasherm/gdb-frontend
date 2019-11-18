# -*- coding: utf-8 -*-
#
# gdb-frontend is a easy, flexible and extensionable gui debugger
#
# https://github.com/rohanrhu/gdb-frontend
# https://oguzhaneroglu.com/projects/gdb-frontend/
#
# Licensed under MIT
# Copyright (C) 2019, Oğuzhan Eroğlu (https://oguzhaneroglu.com/) <rohanrhu2@gmail.com>

import os

VERSION = '0.0.2'
VERBOSE = False
HOST_ADDRESS = "127.0.0.1"
GOTTY_PORT = 5550
HTTP_PORT = 5551
SERVER_PORT = 5552
PLUGINS_DIR = "~/"

gdb_path = os.getcwd()
app_path = os.path.dirname(os.path.realpath(__file__))

urls = {
    "main": {
        "url": "/",
        "match": "^/$",
        "module": "url_modules.main.main"
    },
    "main-layout": {
        "url": "/{layout}/",
        "match": "^/(.+?)/$",
        "module": "url_modules.main.main"
    },
    "api-state": {
        "url": "/api/state",
        "match": "^/api/state$",
        "module": "url_modules.api.state"
    },
    "api-state-get": {
        "url": "/api/state/{info}",
        "match": "^/api/state/(.+)$",
        "module": "url_modules.api.state"
    },
    "api-event": {
        "url": "/api/event",
        "match": "^/api/event$",
        "module": "url_modules.api.event"
    },
    "api-fs-list": {
        "url": "/api/fs/list",
        "match": "^/api/fs/list$",
        "module": "url_modules.api.fs.list"
    },
    "api-fs-read": {
        "url": "/api/fs/read",
        "match": "^/api/fs/read$",
        "module": "url_modules.api.fs.read"
    },
    "api-sources": {
        "url": "/api/sources$",
        "match": "^/api/sources$",
        "module": "url_modules.api.sources"
    },
    "api-breakpoint-add": {
        "url": "/api/breakpoint/add",
        "match": "^/api/breakpoint/add$",
        "module": "url_modules.api.breakpoint.add"
    },
    "api-breakpoint-del": {
        "url": "/api/breakpoint/del",
        "match": "^/api/breakpoint/del$",
        "module": "url_modules.api.breakpoint.del"
    },
    "api-breakpoint-set-enabled": {
        "url": "/api/breakpoint/set_enabled",
        "match": "^/api/breakpoint/set_enabled$",
        "module": "url_modules.api.breakpoint.set_enabled"
    },
    "api-runtime-signal": {
        "url": "/api/runtime/signal",
        "match": "^/api/runtime/signal",
        "module": "url_modules.api.runtime.signal"
    },
    "api-runtime-terminate": {
        "url": "/api/runtime/terminate",
        "match": "^/api/runtime/terminate",
        "module": "url_modules.api.runtime.terminate"
    },
    "api-runtime-run": {
        "url": "/api/runtime/run",
        "match": "^/api/runtime/run$",
        "module": "url_modules.api.runtime.run"
    },
    "api-runtime-pause": {
        "url": "/api/runtime/pause",
        "match": "^/api/runtime/pause$",
        "module": "url_modules.api.runtime.pause"
    },
    "api-runtime-step": {
        "url": "/api/runtime/step",
        "match": "^/api/runtime/step$",
        "module": "url_modules.api.runtime.step"
    },
    "api-runtime-next": {
        "url": "/api/runtime/next",
        "match": "^/api/runtime/next$",
        "module": "url_modules.api.runtime.next"
    },
    "api-runtime-stepi": {
        "url": "/api/runtime/stepi",
        "match": "^/api/runtime/stepi$",
        "module": "url_modules.api.runtime.stepi"
    },
    "api-runtime-continue": {
        "url": "/api/runtime/continue",
        "match": "^/api/runtime/continue$",
        "module": "url_modules.api.runtime.continue"
    },
    "api-thread-switch": {
        "url": "/api/thread/switch",
        "match": "^/api/thread/switch",
        "module": "url_modules.api.thread.switch"
    },
    "api-stack-trace": {
        "url": "/api/stack/trace",
        "match": "^/api/stack/trace",
        "module": "url_modules.api.stack.trace"
    },
    "api-stack-switch": {
        "url": "/api/stack/switch",
        "match": "^/api/stack/switch",
        "module": "url_modules.api.stack.switch"
    },
    "api-frame-variable": {
        "url": "/api/frame/variable",
        "match": "^/api/frame/variable",
        "module": "url_modules.api.frame.variable"
    },
    "api-load": {
        "url": "/api/load",
        "match": "^/api/load$",
        "module": "url_modules.api.load"
    },
    "api-connect": {
        "url": "/api/connect",
        "match": "^/api/connect",
        "module": "url_modules.api.connect"
    },
}
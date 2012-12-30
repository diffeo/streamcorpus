#!/usr/bin/env python
'''
Tools for processing a Stream Corpus
'''

import re
import time
import hashlib
from datetime import datetime
from cStringIO import StringIO

## import the KBA-specific thrift types
from .ttypes import StreamItem, ContentItem, Label, StreamTime, \
    Offset, Rating, Annotator, Versions, Token, Sentence, EntityType, \
    Tagging
from ._chunk import Chunk

def make_stream_time(zulu_timestamp=None):
    '''
    Make a StreamTime object for a zulu_timestamp in this format:
    '2000-01-01T12:34:00.000123Z'
    This computes the equivalent epoch_ticks, so you don't have to.

    If zulu_timestamp is not specified, it defaults to UTC now.
    '''
    zulu_timestamp_format = '%Y-%m-%dT%H:%M:%S.%fZ'
    if zulu_timestamp is None:
        zulu_timestamp = datetime.utcnow().strftime(
            zulu_timestamp_format)
    st = StreamTime(zulu_timestamp=zulu_timestamp)
    ## for reference http://www.epochconverter.com/
    st.epoch_ticks = time.mktime(time.strptime(
            zulu_timestamp, 
            zulu_timestamp_format)) - time.timezone
    ## subtracting the time.timezone is crucial
    return st

def make_stream_item(zulu_timestamp, abs_url):
    '''
    Assemble a minimal StreamItem with internally consistent
    .stream_time.zulu_timestamp, .stream_time.epoch_ticks, .abs_url,
    .doc_id, and .stream_id
    '''
    st = make_stream_time(zulu_timestamp)
    si = StreamItem()
    si.version = Versions.v0_1_0
    si.stream_time = st
    ## Always start with an abs_url and only move it to original_url
    ## if some fetching process decides that the URL needs repair.
    si.abs_url = abs_url
    si.doc_id = hashlib.md5(abs_url).hexdigest()
    si.stream_id = '%d-%s' % (st.epoch_ticks, si.doc_id)
    return si
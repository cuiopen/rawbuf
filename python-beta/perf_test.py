#!/usr/bin/python
#===============================================================================
# NOTE : Generated by rawbuf. It is NOT supposed to modify this file.
#===============================================================================
from rawbuf import *

def rb_create_perf_object():
    return {
        "bool_val" : False,
        "id_bool_val" : 0,
        "skip_bool_val" : False,
        "rb_has_bool_val" : False,
        "int8_val" : 0,
        "id_int8_val" : 1,
        "skip_int8_val" : False,
        "rb_has_int8_val" : False,
        "uint8_val" : 0,
        "id_uint8_val" : 2,
        "skip_uint8_val" : False,
        "rb_has_uint8_val" : False,
        "int16_val" : 0,
        "id_int16_val" : 3,
        "skip_int16_val" : False,
        "rb_has_int16_val" : False,
        "uint16_val" : 0,
        "id_uint16_val" : 4,
        "skip_uint16_val" : False,
        "rb_has_uint16_val" : False,
        "int32_val" : 0,
        "id_int32_val" : 5,
        "skip_int32_val" : False,
        "rb_has_int32_val" : False,
        "uint32_val" : 0,
        "id_uint32_val" : 6,
        "skip_uint32_val" : False,
        "rb_has_uint32_val" : False,
        "int64_val" : 0,
        "id_int64_val" : 7,
        "skip_int64_val" : False,
        "rb_has_int64_val" : False,
        "uint64_val" : 0,
        "id_uint64_val" : 8,
        "skip_uint64_val" : False,
        "rb_has_uint64_val" : False,
        "float_val" : 0.0,
        "id_float_val" : 9,
        "skip_float_val" : False,
        "rb_has_float_val" : False,
        "double_val" : 0.0,
        "id_double_val" : 10,
        "skip_double_val" : False,
        "rb_has_double_val" : False,
        "str_val" : "",
        "id_str_val" : 11,
        "skip_str_val" : False,
        "rb_has_str_val" : False,
        "vec_val" : [],
        "id_vec_val" : 12,
        "skip_vec_val" : False,
        "rb_has_vec_val" : False,
        "dict_val" : {},
        "id_dict_val" : 13,
        "skip_dict_val" : False,
        "rb_has_dict_val" : False
        }

def rb_eq_perf_object(src, dst):
    if src["bool_val"] != dst["bool_val"]:
        return False
    if src["int8_val"] != dst["int8_val"]:
        return False
    if src["uint8_val"] != dst["uint8_val"]:
        return False
    if src["int16_val"] != dst["int16_val"]:
        return False
    if src["uint16_val"] != dst["uint16_val"]:
        return False
    if src["int32_val"] != dst["int32_val"]:
        return False
    if src["uint32_val"] != dst["uint32_val"]:
        return False
    if src["int64_val"] != dst["int64_val"]:
        return False
    if src["uint64_val"] != dst["uint64_val"]:
        return False
    if src["float_val"] != dst["float_val"]:
        return False
    if src["double_val"] != dst["double_val"]:
        return False
    if src["str_val"] != dst["str_val"]:
        return False
    if not rb_eq_int32_array(src["vec_val"], dst["vec_val"]):
        return False
    if not rb_eq_string_dict(src["dict_val"], dst["dict_val"]):
        return False
    return True

def rb_fields_perf_object(obj_val):
    fields = 0
    if not obj_val["skip_bool_val"]:
        fields = fields + 1
    if not obj_val["skip_int8_val"]:
        fields = fields + 1
    if not obj_val["skip_uint8_val"]:
        fields = fields + 1
    if not obj_val["skip_int16_val"]:
        fields = fields + 1
    if not obj_val["skip_uint16_val"]:
        fields = fields + 1
    if not obj_val["skip_int32_val"]:
        fields = fields + 1
    if not obj_val["skip_uint32_val"]:
        fields = fields + 1
    if not obj_val["skip_int64_val"]:
        fields = fields + 1
    if not obj_val["skip_uint64_val"]:
        fields = fields + 1
    if not obj_val["skip_float_val"]:
        fields = fields + 1
    if not obj_val["skip_double_val"]:
        fields = fields + 1
    if not obj_val["skip_str_val"]:
        fields = fields + 1
    if not obj_val["skip_vec_val"]:
        fields = fields + 1
    if not obj_val["skip_dict_val"]:
        fields = fields + 1
    return fields

def rb_sizeof_perf_object(obj_val):
    fields = 0
    size = 0
    if not obj_val["skip_bool_val"]:
        size += rb_sizeof_bool(obj_val["bool_val"])
        fields = fields + 1
    if not obj_val["skip_int8_val"]:
        size += rb_sizeof_int8(obj_val["int8_val"])
        fields = fields + 1
    if not obj_val["skip_uint8_val"]:
        size += rb_sizeof_uint8(obj_val["uint8_val"])
        fields = fields + 1
    if not obj_val["skip_int16_val"]:
        size += rb_sizeof_int16(obj_val["int16_val"])
        fields = fields + 1
    if not obj_val["skip_uint16_val"]:
        size += rb_sizeof_uint16(obj_val["uint16_val"])
        fields = fields + 1
    if not obj_val["skip_int32_val"]:
        size += rb_sizeof_int32(obj_val["int32_val"])
        fields = fields + 1
    if not obj_val["skip_uint32_val"]:
        size += rb_sizeof_uint32(obj_val["uint32_val"])
        fields = fields + 1
    if not obj_val["skip_int64_val"]:
        size += rb_sizeof_int64(obj_val["int64_val"])
        fields = fields + 1
    if not obj_val["skip_uint64_val"]:
        size += rb_sizeof_uint64(obj_val["uint64_val"])
        fields = fields + 1
    if not obj_val["skip_float_val"]:
        size += rb_sizeof_float(obj_val["float_val"])
        fields = fields + 1
    if not obj_val["skip_double_val"]:
        size += rb_sizeof_double(obj_val["double_val"])
        fields = fields + 1
    if not obj_val["skip_str_val"]:
        size += rb_sizeof_string(obj_val["str_val"])
        fields = fields + 1
    if not obj_val["skip_vec_val"]:
        size += rb_sizeof_int32_array(obj_val["vec_val"])
        fields = fields + 1
    if not obj_val["skip_dict_val"]:
        size += rb_sizeof_string_dict(obj_val["dict_val"])
        fields = fields + 1
    size += rb_seek_field_table_item(fields)
    size += sizeof_rb_buf_end
    return size

def rb_encode_perf_object(obj_val, rb_val):
    buf = rb_nested_buf(rb_val, 0)
    if buf["size"] < 1:
        return False
    fields = rb_fields_perf_object(obj_val)
    index = 0
    if not rb_set_field_count(fields, buf):
        return False
    if not obj_val["skip_bool_val"]:
        if not rb_set_field_table_item(index, obj_val["id_bool_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_bool(obj_val["bool_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_int8_val"]:
        if not rb_set_field_table_item(index, obj_val["id_int8_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_int8(obj_val["int8_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_uint8_val"]:
        if not rb_set_field_table_item(index, obj_val["id_uint8_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_uint8(obj_val["uint8_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_int16_val"]:
        if not rb_set_field_table_item(index, obj_val["id_int16_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_int16(obj_val["int16_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_uint16_val"]:
        if not rb_set_field_table_item(index, obj_val["id_uint16_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_uint16(obj_val["uint16_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_int32_val"]:
        if not rb_set_field_table_item(index, obj_val["id_int32_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_int32(obj_val["int32_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_uint32_val"]:
        if not rb_set_field_table_item(index, obj_val["id_uint32_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_uint32(obj_val["uint32_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_int64_val"]:
        if not rb_set_field_table_item(index, obj_val["id_int64_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_int64(obj_val["int64_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_uint64_val"]:
        if not rb_set_field_table_item(index, obj_val["id_uint64_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_uint64(obj_val["uint64_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_float_val"]:
        if not rb_set_field_table_item(index, obj_val["id_float_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_float(obj_val["float_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_double_val"]:
        if not rb_set_field_table_item(index, obj_val["id_double_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_double(obj_val["double_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_str_val"]:
        if not rb_set_field_table_item(index, obj_val["id_str_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_string(obj_val["str_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_vec_val"]:
        if not rb_set_field_table_item(index, obj_val["id_vec_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_int32_array(obj_val["vec_val"], buf):
            return False
        index = index + 1
    if not obj_val["skip_dict_val"]:
        if not rb_set_field_table_item(index, obj_val["id_dict_val"], buf["pos"] - buf["start"], buf):
            return False
        if not rb_encode_string_dict(obj_val["dict_val"], buf):
            return False
        index = index + 1

    if not rb_set_buf_size(buf["pos"] - buf["start"] + sizeof_rb_buf_end, buf):
        return False
    if not rb_encode_end(fields, buf):
        return False
    rb_val["pos"] = buf["pos"]

    return True

def __decode_perf_object(id, offset, rb_val, obj_val):
    if id == obj_val["id_bool_val"]:
        (obj_val["bool_val"], rc) = rb_decode_bool(rb_val, offset)
        if rc: 
            obj_val["rb_has_bool_val"] = True
        return rc
    if id == obj_val["id_int8_val"]:
        (obj_val["int8_val"], rc) = rb_decode_int8(rb_val, offset)
        if rc: 
            obj_val["rb_has_int8_val"] = True
        return rc
    if id == obj_val["id_uint8_val"]:
        (obj_val["uint8_val"], rc) = rb_decode_uint8(rb_val, offset)
        if rc: 
            obj_val["rb_has_uint8_val"] = True
        return rc
    if id == obj_val["id_int16_val"]:
        (obj_val["int16_val"], rc) = rb_decode_int16(rb_val, offset)
        if rc: 
            obj_val["rb_has_int16_val"] = True
        return rc
    if id == obj_val["id_uint16_val"]:
        (obj_val["uint16_val"], rc) = rb_decode_uint16(rb_val, offset)
        if rc: 
            obj_val["rb_has_uint16_val"] = True
        return rc
    if id == obj_val["id_int32_val"]:
        (obj_val["int32_val"], rc) = rb_decode_int32(rb_val, offset)
        if rc: 
            obj_val["rb_has_int32_val"] = True
        return rc
    if id == obj_val["id_uint32_val"]:
        (obj_val["uint32_val"], rc) = rb_decode_uint32(rb_val, offset)
        if rc: 
            obj_val["rb_has_uint32_val"] = True
        return rc
    if id == obj_val["id_int64_val"]:
        (obj_val["int64_val"], rc) = rb_decode_int64(rb_val, offset)
        if rc: 
            obj_val["rb_has_int64_val"] = True
        return rc
    if id == obj_val["id_uint64_val"]:
        (obj_val["uint64_val"], rc) = rb_decode_uint64(rb_val, offset)
        if rc: 
            obj_val["rb_has_uint64_val"] = True
        return rc
    if id == obj_val["id_float_val"]:
        (obj_val["float_val"], rc) = rb_decode_float(rb_val, offset)
        if rc: 
            obj_val["rb_has_float_val"] = True
        return rc
    if id == obj_val["id_double_val"]:
        (obj_val["double_val"], rc) = rb_decode_double(rb_val, offset)
        if rc: 
            obj_val["rb_has_double_val"] = True
        return rc
    if id == obj_val["id_str_val"]:
        (obj_val["str_val"], rc) = rb_decode_string(rb_val, offset)
        if rc: 
            obj_val["rb_has_str_val"] = True
        return rc
    if id == obj_val["id_vec_val"]:
        (obj_val["vec_val"], rc) = rb_decode_int32_array(rb_val, offset)
        if rc: 
            obj_val["rb_has_vec_val"] = True
        return rc
    if id == obj_val["id_dict_val"]:
        (obj_val["dict_val"], rc) = rb_decode_string_dict(rb_val, offset)
        if rc: 
            obj_val["rb_has_dict_val"] = True
        return rc
    return True

def rb_decode_perf_object(rb_val, offset):
    buf = rb_nested_buf(rb_val, offset)
    if buf["size"] < 1:
        return (None, False)
    (size, fields) = rb_get_field_table_head(buf)
    if fields < 1 or not rb_check_code(buf, size, fields):
        return (None, False)
    obj_val = rb_create_perf_object()
    for i in xrange(fields):
        (id, off, rc) = rb_get_field_table_item(i, buf)
        if not rc:
            return (None, False)
        if off >= size:
            return (None, False)
        if off > 0 and not __decode_perf_object(id, off, buf, obj_val):
            return (None, False)
    return (obj_val, True)

def rb_dump_perf_object(obj_val, path):
    size = rb_sizeof_perf_object(obj_val)
    if size < 1:
        return False
    return rb_dump_buf(rb_encode_perf_object, obj_val, size, path)

def rb_load_perf_object(path):
    return rb_load_buf(path, rb_decode_perf_object)

if __name__ == "__main__":
    pass
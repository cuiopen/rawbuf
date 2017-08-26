#!/usr/bin/python
#===============================================================================
# NOTE : Generated by rawbuf. It is NOT supposed to modify this file.
#===============================================================================
from rawbuf import *

class sample_struct_t:
    def __init__(self):
        # fields
        self.int8_val = rb_int8_t()
        self.uint8_val = rb_uint8_t()
        self.str_val = rb_string_t()
        self.str_arr_val = rb_list_t([rb_string_t, None])
        self.str_dict_val = rb_dict_t([rb_string_t, None])
        # ids
        self.__id_int8_val = 0
        self.__id_uint8_val = 1
        self.__id_str_val = 100
        self.__id_str_arr_val = 2
        self.__id_str_dict_val = 3
        # flags
        self.__skip_int8_val = False
        self.__skip_uint8_val = False
        self.__skip_str_val = False
        self.__skip_str_arr_val = False
        self.__skip_str_dict_val = False
        self.__rb_has_int8_val = rb_bool_t()
        self.__rb_has_uint8_val = rb_bool_t()
        self.__rb_has_str_val = rb_bool_t()
        self.__rb_has_str_arr_val = rb_bool_t()
        self.__rb_has_str_dict_val = rb_bool_t()
    def skip_int8_val(self):
        self.__skip_int8_val = True
    def skip_uint8_val(self):
        self.__skip_uint8_val = True
    def skip_str_val(self):
        self.__skip_str_val = True
    def skip_str_arr_val(self):
        self.__skip_str_arr_val = True
    def skip_str_dict_val(self):
        self.__skip_str_dict_val = True
    def rb_has_int8_val(self):
        return self.__rb_has_int8_val.val
    def rb_has_uint8_val(self):
        return self.__rb_has_uint8_val.val
    def rb_has_str_val(self):
        return self.__rb_has_str_val.val
    def rb_has_str_arr_val(self):
        return self.__rb_has_str_arr_val.val
    def rb_has_str_dict_val(self):
        return self.__rb_has_str_dict_val.val
    def __eq__(self, other):
        if not self.int8_val == other.int8_val:
            return False
        if not self.uint8_val == other.uint8_val:
            return False
        if not self.str_val == other.str_val:
            return False
        if not self.str_arr_val == other.str_arr_val:
            return False
        if not self.str_dict_val == other.str_dict_val:
            return False
        return True
    def reset(self):
        self.int8_val.reset()
        self.uint8_val.reset()
        self.str_val.reset()
        self.str_arr_val.reset()
        self.str_dict_val.reset()
    def assign(self, other):
        self.int8_val.assign(other.int8_val)
        self.uint8_val.assign(other.uint8_val)
        self.str_val.assign(other.str_val)
        self.str_arr_val.assign(other.str_arr_val)
        self.str_dict_val.assign(other.str_dict_val)
    def encode(self, buf):
        index = 0
        if not self.__skip_int8_val:
            if not rb_encode_field(index, self.__id_int8_val, self.int8_val, buf):
                return False
            index = index + 1
        if not self.__skip_uint8_val:
            if not rb_encode_field(index, self.__id_uint8_val, self.uint8_val, buf):
                return False
            index = index + 1
        if not self.__skip_str_val:
            if not rb_encode_field(index, self.__id_str_val, self.str_val, buf):
                return False
            index = index + 1
        if not self.__skip_str_arr_val:
            if not rb_encode_field(index, self.__id_str_arr_val, self.str_arr_val, buf):
                return False
            index = index + 1
        if not self.__skip_str_dict_val:
            if not rb_encode_field(index, self.__id_str_dict_val, self.str_dict_val, buf):
                return False
            index = index + 1
        return True
    def decode(self, id, offset, buf):
        rc = rb_bool_t(True)
        if rb_decode_field(self.__id_int8_val, id, offset, buf, rc, self.__rb_has_int8_val, self.int8_val):
            return rc.val
        if rb_decode_field(self.__id_uint8_val, id, offset, buf, rc, self.__rb_has_uint8_val, self.uint8_val):
            return rc.val
        if rb_decode_field(self.__id_str_val, id, offset, buf, rc, self.__rb_has_str_val, self.str_val):
            return rc.val
        if rb_decode_field(self.__id_str_arr_val, id, offset, buf, rc, self.__rb_has_str_arr_val, self.str_arr_val):
            return rc.val
        if rb_decode_field(self.__id_str_dict_val, id, offset, buf, rc, self.__rb_has_str_dict_val, self.str_dict_val):
            return rc.val
        return rc.val
    def rb_fields(self):
        fields = 0
        if not self.__skip_int8_val: fields = fields + 1
        if not self.__skip_uint8_val: fields = fields + 1
        if not self.__skip_str_val: fields = fields + 1
        if not self.__skip_str_arr_val: fields = fields + 1
        if not self.__skip_str_dict_val: fields = fields + 1
        return fields
    def rb_size(self):
        fields = 0
        size = 0
        if not self.__skip_int8_val:
            size += self.int8_val.rb_size()
            fields = fields + 1
        if not self.__skip_uint8_val:
            size += self.uint8_val.rb_size()
            fields = fields + 1
        if not self.__skip_str_val:
            size += self.str_val.rb_size()
            fields = fields + 1
        if not self.__skip_str_arr_val:
            size += self.str_arr_val.rb_size()
            fields = fields + 1
        if not self.__skip_str_dict_val:
            size += self.str_dict_val.rb_size()
            fields = fields + 1
        size += rb_seek_field_table_item(fields)
        size += rb_buf_end_t.rb_size()
        return size
    def rb_encode(self, rb_val):
        return rb_encode_base(self, rb_val)
    def rb_decode(self, rb_val, offset):
        return rb_decode_base(rb_val, offset, self)
    def rb_dump(self, path):
        return rb_dump_base(self, path)
    def rb_load(self, path):
        return rb_load_base(path, self)

class sample_object_t:
    def __init__(self):
        # fields
        self.obj = sample_struct_t()
        self.arr = rb_list_t([sample_struct_t, None])
        self.dict = rb_dict_t([sample_struct_t, None])
        # ids
        self.__id_obj = 0
        self.__id_arr = 1
        self.__id_dict = 2
        # flags
        self.__skip_obj = False
        self.__skip_arr = False
        self.__skip_dict = False
        self.__rb_has_obj = rb_bool_t()
        self.__rb_has_arr = rb_bool_t()
        self.__rb_has_dict = rb_bool_t()
    def skip_obj(self):
        self.__skip_obj = True
    def skip_arr(self):
        self.__skip_arr = True
    def skip_dict(self):
        self.__skip_dict = True
    def rb_has_obj(self):
        return self.__rb_has_obj.val
    def rb_has_arr(self):
        return self.__rb_has_arr.val
    def rb_has_dict(self):
        return self.__rb_has_dict.val
    def __eq__(self, other):
        if not self.obj == other.obj:
            return False
        if not self.arr == other.arr:
            return False
        if not self.dict == other.dict:
            return False
        return True
    def reset(self):
        self.obj.reset()
        self.arr.reset()
        self.dict.reset()
    def assign(self, other):
        self.obj.assign(other.obj)
        self.arr.assign(other.arr)
        self.dict.assign(other.dict)
    def encode(self, buf):
        index = 0
        if not self.__skip_obj:
            if not rb_encode_field(index, self.__id_obj, self.obj, buf):
                return False
            index = index + 1
        if not self.__skip_arr:
            if not rb_encode_field(index, self.__id_arr, self.arr, buf):
                return False
            index = index + 1
        if not self.__skip_dict:
            if not rb_encode_field(index, self.__id_dict, self.dict, buf):
                return False
            index = index + 1
        return True
    def decode(self, id, offset, buf):
        rc = rb_bool_t(True)
        if rb_decode_field(self.__id_obj, id, offset, buf, rc, self.__rb_has_obj, self.obj):
            return rc.val
        if rb_decode_field(self.__id_arr, id, offset, buf, rc, self.__rb_has_arr, self.arr):
            return rc.val
        if rb_decode_field(self.__id_dict, id, offset, buf, rc, self.__rb_has_dict, self.dict):
            return rc.val
        return rc.val
    def rb_fields(self):
        fields = 0
        if not self.__skip_obj: fields = fields + 1
        if not self.__skip_arr: fields = fields + 1
        if not self.__skip_dict: fields = fields + 1
        return fields
    def rb_size(self):
        fields = 0
        size = 0
        if not self.__skip_obj:
            size += self.obj.rb_size()
            fields = fields + 1
        if not self.__skip_arr:
            size += self.arr.rb_size()
            fields = fields + 1
        if not self.__skip_dict:
            size += self.dict.rb_size()
            fields = fields + 1
        size += rb_seek_field_table_item(fields)
        size += rb_buf_end_t.rb_size()
        return size
    def rb_encode(self, rb_val):
        return rb_encode_base(self, rb_val)
    def rb_decode(self, rb_val, offset):
        return rb_decode_base(rb_val, offset, self)
    def rb_dump(self, path):
        return rb_dump_base(self, path)
    def rb_load(self, path):
        return rb_load_base(path, self)

if __name__ == "__main__":
    pass
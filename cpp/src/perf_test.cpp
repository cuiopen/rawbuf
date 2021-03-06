////////////////////////////////////////////////////////////////////////////////
// NOTE : Generated by rawbuf. It is NOT supposed to modify this file.
////////////////////////////////////////////////////////////////////////////////
#include "perf_test.h"

namespace rawbuf {

perf_object_t::perf_object_t()
{
    bool_val = false;
    __id_bool_val = 0;
    __skip_bool_val = false;
    __rb_has_bool_val = false;

    int8_val = 0;
    __id_int8_val = 1;
    __skip_int8_val = false;
    __rb_has_int8_val = false;

    uint8_val = 0;
    __id_uint8_val = 2;
    __skip_uint8_val = false;
    __rb_has_uint8_val = false;

    int16_val = 0;
    __id_int16_val = 3;
    __skip_int16_val = false;
    __rb_has_int16_val = false;

    uint16_val = 0;
    __id_uint16_val = 4;
    __skip_uint16_val = false;
    __rb_has_uint16_val = false;

    int32_val = 0;
    __id_int32_val = 5;
    __skip_int32_val = false;
    __rb_has_int32_val = false;

    uint32_val = 0;
    __id_uint32_val = 6;
    __skip_uint32_val = false;
    __rb_has_uint32_val = false;

    int64_val = 0;
    __id_int64_val = 7;
    __skip_int64_val = false;
    __rb_has_int64_val = false;

    uint64_val = 0;
    __id_uint64_val = 8;
    __skip_uint64_val = false;
    __rb_has_uint64_val = false;

    float_val = 0.0;
    __id_float_val = 9;
    __skip_float_val = false;
    __rb_has_float_val = false;

    double_val = 0.0;
    __id_double_val = 10;
    __skip_double_val = false;
    __rb_has_double_val = false;

    __id_str_val = 11;
    __skip_str_val = false;
    __rb_has_str_val = false;

    __id_vec_val = 12;
    __skip_vec_val = false;
    __rb_has_vec_val = false;

    __id_dict_val = 13;
    __skip_dict_val = false;
    __rb_has_dict_val = false;
}

perf_object_t& perf_object_t::operator=(const perf_object_t& obj_val)
{
    this->bool_val = obj_val.bool_val;
    this->int8_val = obj_val.int8_val;
    this->uint8_val = obj_val.uint8_val;
    this->int16_val = obj_val.int16_val;
    this->uint16_val = obj_val.uint16_val;
    this->int32_val = obj_val.int32_val;
    this->uint32_val = obj_val.uint32_val;
    this->int64_val = obj_val.int64_val;
    this->uint64_val = obj_val.uint64_val;
    this->float_val = obj_val.float_val;
    this->double_val = obj_val.double_val;
    this->str_val = obj_val.str_val;
    this->vec_val = obj_val.vec_val;
    this->dict_val = obj_val.dict_val;
    return *this;
}

bool perf_object_t::operator==(const perf_object_t& obj_val) const
{
    if (!(this->bool_val == obj_val.bool_val)) return false;
    if (!(this->int8_val == obj_val.int8_val)) return false;
    if (!(this->uint8_val == obj_val.uint8_val)) return false;
    if (!(this->int16_val == obj_val.int16_val)) return false;
    if (!(this->uint16_val == obj_val.uint16_val)) return false;
    if (!(this->int32_val == obj_val.int32_val)) return false;
    if (!(this->uint32_val == obj_val.uint32_val)) return false;
    if (!(this->int64_val == obj_val.int64_val)) return false;
    if (!(this->uint64_val == obj_val.uint64_val)) return false;
    if (!(this->float_val == obj_val.float_val)) return false;
    if (!(this->double_val == obj_val.double_val)) return false;
    if (!(this->str_val == obj_val.str_val)) return false;
    if (!(this->vec_val == obj_val.vec_val)) return false;
    if (!(this->dict_val == obj_val.dict_val)) return false;
    return true;
}

rb_field_size_t perf_object_t::rb_fields() const
{
    rb_field_size_t fields = 0;
    if (!__skip_bool_val) ++fields;
    if (!__skip_int8_val) ++fields;
    if (!__skip_uint8_val) ++fields;
    if (!__skip_int16_val) ++fields;
    if (!__skip_uint16_val) ++fields;
    if (!__skip_int32_val) ++fields;
    if (!__skip_uint32_val) ++fields;
    if (!__skip_int64_val) ++fields;
    if (!__skip_uint64_val) ++fields;
    if (!__skip_float_val) ++fields;
    if (!__skip_double_val) ++fields;
    if (!__skip_str_val) ++fields;
    if (!__skip_vec_val) ++fields;
    if (!__skip_dict_val) ++fields;
    return fields;
}

rb_size_t perf_object_t::rb_size() const
{
    rb_field_size_t fields = 0;
    rb_size_t size = 0;
    if (!__skip_bool_val)
    {
        size += rb_sizeof(bool_val);
        ++fields;
    }
    if (!__skip_int8_val)
    {
        size += rb_sizeof(int8_val);
        ++fields;
    }
    if (!__skip_uint8_val)
    {
        size += rb_sizeof(uint8_val);
        ++fields;
    }
    if (!__skip_int16_val)
    {
        size += rb_sizeof(int16_val);
        ++fields;
    }
    if (!__skip_uint16_val)
    {
        size += rb_sizeof(uint16_val);
        ++fields;
    }
    if (!__skip_int32_val)
    {
        size += rb_sizeof(int32_val);
        ++fields;
    }
    if (!__skip_uint32_val)
    {
        size += rb_sizeof(uint32_val);
        ++fields;
    }
    if (!__skip_int64_val)
    {
        size += rb_sizeof(int64_val);
        ++fields;
    }
    if (!__skip_uint64_val)
    {
        size += rb_sizeof(uint64_val);
        ++fields;
    }
    if (!__skip_float_val)
    {
        size += rb_sizeof(float_val);
        ++fields;
    }
    if (!__skip_double_val)
    {
        size += rb_sizeof(double_val);
        ++fields;
    }
    if (!__skip_str_val)
    {
        size += rb_sizeof(str_val);
        ++fields;
    }
    if (!__skip_vec_val)
    {
        size += rb_sizeof(vec_val);
        ++fields;
    }
    if (!__skip_dict_val)
    {
        size += rb_sizeof(dict_val);
        ++fields;
    }
    size += rb_seek_field_table_item(fields);
    size += sizeof(rb_buf_end_t);
    return size;
}

bool perf_object_t::encode(rb_buf_t& buf) const
{
    rb_field_size_t index = 0;
    if (!__skip_bool_val && !rb_encode_field(index++, __id_bool_val, bool_val, buf)) return false;
    if (!__skip_int8_val && !rb_encode_field(index++, __id_int8_val, int8_val, buf)) return false;
    if (!__skip_uint8_val && !rb_encode_field(index++, __id_uint8_val, uint8_val, buf)) return false;
    if (!__skip_int16_val && !rb_encode_field(index++, __id_int16_val, int16_val, buf)) return false;
    if (!__skip_uint16_val && !rb_encode_field(index++, __id_uint16_val, uint16_val, buf)) return false;
    if (!__skip_int32_val && !rb_encode_field(index++, __id_int32_val, int32_val, buf)) return false;
    if (!__skip_uint32_val && !rb_encode_field(index++, __id_uint32_val, uint32_val, buf)) return false;
    if (!__skip_int64_val && !rb_encode_field(index++, __id_int64_val, int64_val, buf)) return false;
    if (!__skip_uint64_val && !rb_encode_field(index++, __id_uint64_val, uint64_val, buf)) return false;
    if (!__skip_float_val && !rb_encode_field(index++, __id_float_val, float_val, buf)) return false;
    if (!__skip_double_val && !rb_encode_field(index++, __id_double_val, double_val, buf)) return false;
    if (!__skip_str_val && !rb_encode_field(index++, __id_str_val, str_val, buf)) return false;
    if (!__skip_vec_val && !rb_encode_field(index++, __id_vec_val, vec_val, buf)) return false;
    if (!__skip_dict_val && !rb_encode_field(index++, __id_dict_val, dict_val, buf)) return false;
    return true;
}

bool perf_object_t::decode(const rb_field_table_item_t& item, const rb_buf_t& buf)
{
    bool rc = true;
    do
    {
        if (rb_decode_field(__id_bool_val, item, buf, rc, __rb_has_bool_val, bool_val)) break;
        if (rb_decode_field(__id_int8_val, item, buf, rc, __rb_has_int8_val, int8_val)) break;
        if (rb_decode_field(__id_uint8_val, item, buf, rc, __rb_has_uint8_val, uint8_val)) break;
        if (rb_decode_field(__id_int16_val, item, buf, rc, __rb_has_int16_val, int16_val)) break;
        if (rb_decode_field(__id_uint16_val, item, buf, rc, __rb_has_uint16_val, uint16_val)) break;
        if (rb_decode_field(__id_int32_val, item, buf, rc, __rb_has_int32_val, int32_val)) break;
        if (rb_decode_field(__id_uint32_val, item, buf, rc, __rb_has_uint32_val, uint32_val)) break;
        if (rb_decode_field(__id_int64_val, item, buf, rc, __rb_has_int64_val, int64_val)) break;
        if (rb_decode_field(__id_uint64_val, item, buf, rc, __rb_has_uint64_val, uint64_val)) break;
        if (rb_decode_field(__id_float_val, item, buf, rc, __rb_has_float_val, float_val)) break;
        if (rb_decode_field(__id_double_val, item, buf, rc, __rb_has_double_val, double_val)) break;
        if (rb_decode_field(__id_str_val, item, buf, rc, __rb_has_str_val, str_val)) break;
        if (rb_decode_field(__id_vec_val, item, buf, rc, __rb_has_vec_val, vec_val)) break;
        if (rb_decode_field(__id_dict_val, item, buf, rc, __rb_has_dict_val, dict_val)) break;
    } while (0);
    return rc;
}

rb_size_t rb_sizeof(const perf_object_t& obj_val)
{
    return obj_val.rb_size();
}

bool rb_encode(const perf_object_t& obj_val, rb_buf_t& rb_val)
{
    return rb_encode_base(obj_val, rb_val);
}

bool rb_decode(const rb_buf_t& rb_val, rb_offset_t offset, perf_object_t& obj_val)
{
    return rb_decode_base(rb_val, offset, obj_val);
}

bool rb_dump(const perf_object_t& obj_val, const char * path)
{
    return rb_dump_base(obj_val, path);
}

bool rb_load(const char * path, perf_object_t& obj_val)
{
    return rb_load_base(path, obj_val);
}

} // namespace rawbuf
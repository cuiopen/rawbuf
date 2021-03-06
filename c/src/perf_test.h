////////////////////////////////////////////////////////////////////////////////
// NOTE : Generated by rawbuf. It is NOT supposed to modify this file.
////////////////////////////////////////////////////////////////////////////////
#ifndef __perf_test_20160604101630_h__
#define __perf_test_20160604101630_h__

#include "rawbuf.h"

typedef struct
{
    rb_bool_t bool_val;
    int8_t int8_val;
    uint8_t uint8_val;
    int16_t int16_val;
    uint16_t uint16_val;
    int32_t int32_val;
    uint32_t uint32_val;
    int64_t int64_val;
    uint64_t uint64_val;
    float float_val;
    double double_val;
    rb_str_t str_val;
    int32_array_t vec_val;
    string_dict_t dict_val;

    rb_field_id_t id_bool_val;
    rb_field_id_t id_int8_val;
    rb_field_id_t id_uint8_val;
    rb_field_id_t id_int16_val;
    rb_field_id_t id_uint16_val;
    rb_field_id_t id_int32_val;
    rb_field_id_t id_uint32_val;
    rb_field_id_t id_int64_val;
    rb_field_id_t id_uint64_val;
    rb_field_id_t id_float_val;
    rb_field_id_t id_double_val;
    rb_field_id_t id_str_val;
    rb_field_id_t id_vec_val;
    rb_field_id_t id_dict_val;

    rb_bool_t skip_bool_val;
    rb_bool_t skip_int8_val;
    rb_bool_t skip_uint8_val;
    rb_bool_t skip_int16_val;
    rb_bool_t skip_uint16_val;
    rb_bool_t skip_int32_val;
    rb_bool_t skip_uint32_val;
    rb_bool_t skip_int64_val;
    rb_bool_t skip_uint64_val;
    rb_bool_t skip_float_val;
    rb_bool_t skip_double_val;
    rb_bool_t skip_str_val;
    rb_bool_t skip_vec_val;
    rb_bool_t skip_dict_val;

    rb_bool_t rb_has_bool_val;
    rb_bool_t rb_has_int8_val;
    rb_bool_t rb_has_uint8_val;
    rb_bool_t rb_has_int16_val;
    rb_bool_t rb_has_uint16_val;
    rb_bool_t rb_has_int32_val;
    rb_bool_t rb_has_uint32_val;
    rb_bool_t rb_has_int64_val;
    rb_bool_t rb_has_uint64_val;
    rb_bool_t rb_has_float_val;
    rb_bool_t rb_has_double_val;
    rb_bool_t rb_has_str_val;
    rb_bool_t rb_has_vec_val;
    rb_bool_t rb_has_dict_val;
} perf_object_t;

void rb_init_perf_object(perf_object_t * obj_val);
rb_bool_t rb_set_perf_object(const perf_object_t * src, perf_object_t * dst);
rb_bool_t rb_eq_perf_object(const perf_object_t * src, const perf_object_t * dst);
void rb_dispose_perf_object(perf_object_t * obj_val);
rb_field_size_t rb_fields_perf_object(const perf_object_t * obj_val);
rb_size_t rb_sizeof_perf_object(const perf_object_t * obj_val);
rb_bool_t rb_encode_perf_object(const perf_object_t * obj_val, rb_buf_t * rb_val);
rb_bool_t rb_decode_perf_object(const rb_buf_t * rb_val, rb_offset_t offset, perf_object_t * obj_val);
rb_bool_t rb_dump_perf_object(const perf_object_t * obj_val, const char * path);
rb_bool_t rb_load_perf_object(const char * path, perf_object_t * obj_val);

#endif // __perf_test_20160604101630_h__
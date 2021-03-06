////////////////////////////////////////////////////////////////////////////////
// NOTE : Generated by rawbuf. It is NOT supposed to modify this file.
////////////////////////////////////////////////////////////////////////////////
#ifndef __sample_test_20160820040110_h__
#define __sample_test_20160820040110_h__

#include "rawbuf.h"

typedef struct
{
    int8_t int8_val;
    uint8_t uint8_val;
    rb_str_t str_val;
    string_array_t str_arr_val;
    string_dict_t str_dict_val;

    rb_field_id_t id_int8_val;
    rb_field_id_t id_uint8_val;
    rb_field_id_t id_str_val;
    rb_field_id_t id_str_arr_val;
    rb_field_id_t id_str_dict_val;

    rb_bool_t skip_int8_val;
    rb_bool_t skip_uint8_val;
    rb_bool_t skip_str_val;
    rb_bool_t skip_str_arr_val;
    rb_bool_t skip_str_dict_val;

    rb_bool_t rb_has_int8_val;
    rb_bool_t rb_has_uint8_val;
    rb_bool_t rb_has_str_val;
    rb_bool_t rb_has_str_arr_val;
    rb_bool_t rb_has_str_dict_val;
} sample_struct_t;

void rb_init_sample_struct(sample_struct_t * obj_val);
rb_bool_t rb_set_sample_struct(const sample_struct_t * src, sample_struct_t * dst);
rb_bool_t rb_eq_sample_struct(const sample_struct_t * src, const sample_struct_t * dst);
void rb_dispose_sample_struct(sample_struct_t * obj_val);
rb_field_size_t rb_fields_sample_struct(const sample_struct_t * obj_val);
rb_size_t rb_sizeof_sample_struct(const sample_struct_t * obj_val);
rb_bool_t rb_encode_sample_struct(const sample_struct_t * obj_val, rb_buf_t * rb_val);
rb_bool_t rb_decode_sample_struct(const rb_buf_t * rb_val, rb_offset_t offset, sample_struct_t * obj_val);
rb_bool_t rb_dump_sample_struct(const sample_struct_t * obj_val, const char * path);
rb_bool_t rb_load_sample_struct(const char * path, sample_struct_t * obj_val);

typedef struct
{
    rb_size_t capacity;
    rb_size_t size;
    sample_struct_t * arr;
} sample_struct_array_t;

sample_struct_array_t rb_create_sample_struct_array(rb_size_t capacity);
rb_bool_t rb_append_to_sample_struct_array(const sample_struct_t * item, sample_struct_array_t * obj_val);
void rb_init_sample_struct_array(sample_struct_array_t * obj_val);
rb_bool_t rb_set_sample_struct_array(const sample_struct_array_t * src, sample_struct_array_t * dst);
rb_bool_t rb_eq_sample_struct_array(const sample_struct_array_t * src, const sample_struct_array_t * dst);
void rb_dispose_sample_struct_array(sample_struct_array_t * obj_val);
rb_size_t rb_sizeof_sample_struct_array(const sample_struct_array_t * obj_val);
rb_bool_t rb_encode_sample_struct_array(const sample_struct_array_t * obj_val, rb_buf_t * rb_val);
rb_bool_t rb_decode_sample_struct_array(const rb_buf_t * rb_val, rb_offset_t offset, sample_struct_array_t * obj_val);

typedef struct
{
    rb_str_t key;
    sample_struct_t val;
} sample_struct_pair_t;

typedef struct
{
    rb_size_t capacity;
    rb_size_t size;
    sample_struct_pair_t * arr;
} sample_struct_dict_t;

sample_struct_dict_t rb_create_sample_struct_dict(rb_size_t capacity);
sample_struct_pair_t * rb_sample_struct_dict_get_item(const sample_struct_dict_t * obj_val, const rb_str_t * key);
rb_bool_t rb_sample_struct_dict_set_item(const rb_str_t * key, const sample_struct_t * val, sample_struct_dict_t * obj_val);
void rb_init_sample_struct_dict(sample_struct_dict_t * obj_val);
rb_bool_t rb_set_sample_struct_dict(const sample_struct_dict_t * src, sample_struct_dict_t * dst);
rb_bool_t rb_eq_sample_struct_dict(const sample_struct_dict_t * src, const sample_struct_dict_t * dst);
void rb_dispose_sample_struct_dict(sample_struct_dict_t * obj_val);
rb_size_t rb_sizeof_sample_struct_dict(const sample_struct_dict_t * obj_val);
rb_bool_t rb_encode_sample_struct_dict(const sample_struct_dict_t * obj_val, rb_buf_t * rb_val);
rb_bool_t rb_decode_sample_struct_dict(const rb_buf_t * rb_val, rb_offset_t offset, sample_struct_dict_t * obj_val);

typedef struct
{
    sample_struct_t obj;
    sample_struct_array_t arr;
    sample_struct_dict_t dict;

    rb_field_id_t id_obj;
    rb_field_id_t id_arr;
    rb_field_id_t id_dict;

    rb_bool_t skip_obj;
    rb_bool_t skip_arr;
    rb_bool_t skip_dict;

    rb_bool_t rb_has_obj;
    rb_bool_t rb_has_arr;
    rb_bool_t rb_has_dict;
} sample_object_t;

void rb_init_sample_object(sample_object_t * obj_val);
rb_bool_t rb_set_sample_object(const sample_object_t * src, sample_object_t * dst);
rb_bool_t rb_eq_sample_object(const sample_object_t * src, const sample_object_t * dst);
void rb_dispose_sample_object(sample_object_t * obj_val);
rb_field_size_t rb_fields_sample_object(const sample_object_t * obj_val);
rb_size_t rb_sizeof_sample_object(const sample_object_t * obj_val);
rb_bool_t rb_encode_sample_object(const sample_object_t * obj_val, rb_buf_t * rb_val);
rb_bool_t rb_decode_sample_object(const rb_buf_t * rb_val, rb_offset_t offset, sample_object_t * obj_val);
rb_bool_t rb_dump_sample_object(const sample_object_t * obj_val, const char * path);
rb_bool_t rb_load_sample_object(const char * path, sample_object_t * obj_val);

#endif // __sample_test_20160820040110_h__
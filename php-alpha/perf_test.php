<?php
////////////////////////////////////////////////////////////////////////////////
// NOTE : Generated by rawbuf. It is NOT supposed to modify this file.
////////////////////////////////////////////////////////////////////////////////

require_once "rawbuf.php";

class perf_object_t
{
    // fields
    public $bool_val;
    public $int8_val;
    public $uint8_val;
    public $int16_val;
    public $uint16_val;
    public $int32_val;
    public $uint32_val;
    public $int64_val;
    public $uint64_val;
    public $float_val;
    public $double_val;
    public $str_val;
    public $vec_val;
    public $dict_val;
    // ids
    private $__id_bool_val;
    private $__id_int8_val;
    private $__id_uint8_val;
    private $__id_int16_val;
    private $__id_uint16_val;
    private $__id_int32_val;
    private $__id_uint32_val;
    private $__id_int64_val;
    private $__id_uint64_val;
    private $__id_float_val;
    private $__id_double_val;
    private $__id_str_val;
    private $__id_vec_val;
    private $__id_dict_val;
    // flags
    private $__skip_bool_val;
    private $__skip_int8_val;
    private $__skip_uint8_val;
    private $__skip_int16_val;
    private $__skip_uint16_val;
    private $__skip_int32_val;
    private $__skip_uint32_val;
    private $__skip_int64_val;
    private $__skip_uint64_val;
    private $__skip_float_val;
    private $__skip_double_val;
    private $__skip_str_val;
    private $__skip_vec_val;
    private $__skip_dict_val;
    private $__rb_has_bool_val;
    private $__rb_has_int8_val;
    private $__rb_has_uint8_val;
    private $__rb_has_int16_val;
    private $__rb_has_uint16_val;
    private $__rb_has_int32_val;
    private $__rb_has_uint32_val;
    private $__rb_has_int64_val;
    private $__rb_has_uint64_val;
    private $__rb_has_float_val;
    private $__rb_has_double_val;
    private $__rb_has_str_val;
    private $__rb_has_vec_val;
    private $__rb_has_dict_val;
    public function __construct()
    {
        // fields
        $this->bool_val = new rb_bool_t();
        $this->int8_val = new rb_int8_t();
        $this->uint8_val = new rb_uint8_t();
        $this->int16_val = new rb_int16_t();
        $this->uint16_val = new rb_uint16_t();
        $this->int32_val = new rb_int32_t();
        $this->uint32_val = new rb_uint32_t();
        $this->int64_val = new rb_int64_t();
        $this->uint64_val = new rb_uint64_t();
        $this->float_val = new rb_float_t();
        $this->double_val = new rb_double_t();
        $this->str_val = new rb_string_t();
        $this->vec_val = new rb_list_t(array(rb_int32_t, null));
        $this->dict_val = new rb_dict_t(array(rb_string_t, null));
        // ids
        $this->__id_bool_val = 0;
        $this->__id_int8_val = 1;
        $this->__id_uint8_val = 2;
        $this->__id_int16_val = 3;
        $this->__id_uint16_val = 4;
        $this->__id_int32_val = 5;
        $this->__id_uint32_val = 6;
        $this->__id_int64_val = 7;
        $this->__id_uint64_val = 8;
        $this->__id_float_val = 9;
        $this->__id_double_val = 10;
        $this->__id_str_val = 11;
        $this->__id_vec_val = 12;
        $this->__id_dict_val = 13;
        // flags
        $this->__skip_bool_val = false;
        $this->__skip_int8_val = false;
        $this->__skip_uint8_val = false;
        $this->__skip_int16_val = false;
        $this->__skip_uint16_val = false;
        $this->__skip_int32_val = false;
        $this->__skip_uint32_val = false;
        $this->__skip_int64_val = false;
        $this->__skip_uint64_val = false;
        $this->__skip_float_val = false;
        $this->__skip_double_val = false;
        $this->__skip_str_val = false;
        $this->__skip_vec_val = false;
        $this->__skip_dict_val = false;
        $this->__rb_has_bool_val = new rb_bool_t();
        $this->__rb_has_int8_val = new rb_bool_t();
        $this->__rb_has_uint8_val = new rb_bool_t();
        $this->__rb_has_int16_val = new rb_bool_t();
        $this->__rb_has_uint16_val = new rb_bool_t();
        $this->__rb_has_int32_val = new rb_bool_t();
        $this->__rb_has_uint32_val = new rb_bool_t();
        $this->__rb_has_int64_val = new rb_bool_t();
        $this->__rb_has_uint64_val = new rb_bool_t();
        $this->__rb_has_float_val = new rb_bool_t();
        $this->__rb_has_double_val = new rb_bool_t();
        $this->__rb_has_str_val = new rb_bool_t();
        $this->__rb_has_vec_val = new rb_bool_t();
        $this->__rb_has_dict_val = new rb_bool_t();
    }
    public function skip_bool_val()
    {
        $this->__skip_bool_val = true;
    }
    public function skip_int8_val()
    {
        $this->__skip_int8_val = true;
    }
    public function skip_uint8_val()
    {
        $this->__skip_uint8_val = true;
    }
    public function skip_int16_val()
    {
        $this->__skip_int16_val = true;
    }
    public function skip_uint16_val()
    {
        $this->__skip_uint16_val = true;
    }
    public function skip_int32_val()
    {
        $this->__skip_int32_val = true;
    }
    public function skip_uint32_val()
    {
        $this->__skip_uint32_val = true;
    }
    public function skip_int64_val()
    {
        $this->__skip_int64_val = true;
    }
    public function skip_uint64_val()
    {
        $this->__skip_uint64_val = true;
    }
    public function skip_float_val()
    {
        $this->__skip_float_val = true;
    }
    public function skip_double_val()
    {
        $this->__skip_double_val = true;
    }
    public function skip_str_val()
    {
        $this->__skip_str_val = true;
    }
    public function skip_vec_val()
    {
        $this->__skip_vec_val = true;
    }
    public function skip_dict_val()
    {
        $this->__skip_dict_val = true;
    }
    public function rb_has_bool_val()
    {
        return $this->__rb_has_bool_val->val;
    }
    public function rb_has_int8_val()
    {
        return $this->__rb_has_int8_val->val;
    }
    public function rb_has_uint8_val()
    {
        return $this->__rb_has_uint8_val->val;
    }
    public function rb_has_int16_val()
    {
        return $this->__rb_has_int16_val->val;
    }
    public function rb_has_uint16_val()
    {
        return $this->__rb_has_uint16_val->val;
    }
    public function rb_has_int32_val()
    {
        return $this->__rb_has_int32_val->val;
    }
    public function rb_has_uint32_val()
    {
        return $this->__rb_has_uint32_val->val;
    }
    public function rb_has_int64_val()
    {
        return $this->__rb_has_int64_val->val;
    }
    public function rb_has_uint64_val()
    {
        return $this->__rb_has_uint64_val->val;
    }
    public function rb_has_float_val()
    {
        return $this->__rb_has_float_val->val;
    }
    public function rb_has_double_val()
    {
        return $this->__rb_has_double_val->val;
    }
    public function rb_has_str_val()
    {
        return $this->__rb_has_str_val->val;
    }
    public function rb_has_vec_val()
    {
        return $this->__rb_has_vec_val->val;
    }
    public function rb_has_dict_val()
    {
        return $this->__rb_has_dict_val->val;
    }
    public function eq($other)
    {
        if (!$this->bool_val->eq($other->bool_val)) return false;
        if (!$this->int8_val->eq($other->int8_val)) return false;
        if (!$this->uint8_val->eq($other->uint8_val)) return false;
        if (!$this->int16_val->eq($other->int16_val)) return false;
        if (!$this->uint16_val->eq($other->uint16_val)) return false;
        if (!$this->int32_val->eq($other->int32_val)) return false;
        if (!$this->uint32_val->eq($other->uint32_val)) return false;
        if (!$this->int64_val->eq($other->int64_val)) return false;
        if (!$this->uint64_val->eq($other->uint64_val)) return false;
        if (!$this->float_val->eq($other->float_val)) return false;
        if (!$this->double_val->eq($other->double_val)) return false;
        if (!$this->str_val->eq($other->str_val)) return false;
        if (!$this->vec_val->eq($other->vec_val)) return false;
        if (!$this->dict_val->eq($other->dict_val)) return false;
        return true;
    }
    public function reset()
    {
        $this->bool_val->reset();
        $this->int8_val->reset();
        $this->uint8_val->reset();
        $this->int16_val->reset();
        $this->uint16_val->reset();
        $this->int32_val->reset();
        $this->uint32_val->reset();
        $this->int64_val->reset();
        $this->uint64_val->reset();
        $this->float_val->reset();
        $this->double_val->reset();
        $this->str_val->reset();
        $this->vec_val->reset();
        $this->dict_val->reset();
    }
    public function assign($other)
    {
        $this->bool_val->assign($other->bool_val);
        $this->int8_val->assign($other->int8_val);
        $this->uint8_val->assign($other->uint8_val);
        $this->int16_val->assign($other->int16_val);
        $this->uint16_val->assign($other->uint16_val);
        $this->int32_val->assign($other->int32_val);
        $this->uint32_val->assign($other->uint32_val);
        $this->int64_val->assign($other->int64_val);
        $this->uint64_val->assign($other->uint64_val);
        $this->float_val->assign($other->float_val);
        $this->double_val->assign($other->double_val);
        $this->str_val->assign($other->str_val);
        $this->vec_val->assign($other->vec_val);
        $this->dict_val->assign($other->dict_val);
    }
    public function encode($buf)
    {
        $index = 0;
        if (!$this->__skip_bool_val && !rb_encode_field($index++, $this->__id_bool_val, $this->bool_val, $buf)) return false;
        if (!$this->__skip_int8_val && !rb_encode_field($index++, $this->__id_int8_val, $this->int8_val, $buf)) return false;
        if (!$this->__skip_uint8_val && !rb_encode_field($index++, $this->__id_uint8_val, $this->uint8_val, $buf)) return false;
        if (!$this->__skip_int16_val && !rb_encode_field($index++, $this->__id_int16_val, $this->int16_val, $buf)) return false;
        if (!$this->__skip_uint16_val && !rb_encode_field($index++, $this->__id_uint16_val, $this->uint16_val, $buf)) return false;
        if (!$this->__skip_int32_val && !rb_encode_field($index++, $this->__id_int32_val, $this->int32_val, $buf)) return false;
        if (!$this->__skip_uint32_val && !rb_encode_field($index++, $this->__id_uint32_val, $this->uint32_val, $buf)) return false;
        if (!$this->__skip_int64_val && !rb_encode_field($index++, $this->__id_int64_val, $this->int64_val, $buf)) return false;
        if (!$this->__skip_uint64_val && !rb_encode_field($index++, $this->__id_uint64_val, $this->uint64_val, $buf)) return false;
        if (!$this->__skip_float_val && !rb_encode_field($index++, $this->__id_float_val, $this->float_val, $buf)) return false;
        if (!$this->__skip_double_val && !rb_encode_field($index++, $this->__id_double_val, $this->double_val, $buf)) return false;
        if (!$this->__skip_str_val && !rb_encode_field($index++, $this->__id_str_val, $this->str_val, $buf)) return false;
        if (!$this->__skip_vec_val && !rb_encode_field($index++, $this->__id_vec_val, $this->vec_val, $buf)) return false;
        if (!$this->__skip_dict_val && !rb_encode_field($index++, $this->__id_dict_val, $this->dict_val, $buf)) return false;
        return true;
    }
    public function decode($id, $offset, $buf)
    {
        $rc = new rb_bool_t(true);
        if (rb_decode_field($this->__id_bool_val, $id, $offset, $buf, $rc, $this->__rb_has_bool_val, $this->bool_val)) return $rc->val;
        if (rb_decode_field($this->__id_int8_val, $id, $offset, $buf, $rc, $this->__rb_has_int8_val, $this->int8_val)) return $rc->val;
        if (rb_decode_field($this->__id_uint8_val, $id, $offset, $buf, $rc, $this->__rb_has_uint8_val, $this->uint8_val)) return $rc->val;
        if (rb_decode_field($this->__id_int16_val, $id, $offset, $buf, $rc, $this->__rb_has_int16_val, $this->int16_val)) return $rc->val;
        if (rb_decode_field($this->__id_uint16_val, $id, $offset, $buf, $rc, $this->__rb_has_uint16_val, $this->uint16_val)) return $rc->val;
        if (rb_decode_field($this->__id_int32_val, $id, $offset, $buf, $rc, $this->__rb_has_int32_val, $this->int32_val)) return $rc->val;
        if (rb_decode_field($this->__id_uint32_val, $id, $offset, $buf, $rc, $this->__rb_has_uint32_val, $this->uint32_val)) return $rc->val;
        if (rb_decode_field($this->__id_int64_val, $id, $offset, $buf, $rc, $this->__rb_has_int64_val, $this->int64_val)) return $rc->val;
        if (rb_decode_field($this->__id_uint64_val, $id, $offset, $buf, $rc, $this->__rb_has_uint64_val, $this->uint64_val)) return $rc->val;
        if (rb_decode_field($this->__id_float_val, $id, $offset, $buf, $rc, $this->__rb_has_float_val, $this->float_val)) return $rc->val;
        if (rb_decode_field($this->__id_double_val, $id, $offset, $buf, $rc, $this->__rb_has_double_val, $this->double_val)) return $rc->val;
        if (rb_decode_field($this->__id_str_val, $id, $offset, $buf, $rc, $this->__rb_has_str_val, $this->str_val)) return $rc->val;
        if (rb_decode_field($this->__id_vec_val, $id, $offset, $buf, $rc, $this->__rb_has_vec_val, $this->vec_val)) return $rc->val;
        if (rb_decode_field($this->__id_dict_val, $id, $offset, $buf, $rc, $this->__rb_has_dict_val, $this->dict_val)) return $rc->val;
        return $rc->val;
    }
    public function rb_fields()
    {
        $fields = 0;
        if (!$this->__skip_bool_val) $fields++;
        if (!$this->__skip_int8_val) $fields++;
        if (!$this->__skip_uint8_val) $fields++;
        if (!$this->__skip_int16_val) $fields++;
        if (!$this->__skip_uint16_val) $fields++;
        if (!$this->__skip_int32_val) $fields++;
        if (!$this->__skip_uint32_val) $fields++;
        if (!$this->__skip_int64_val) $fields++;
        if (!$this->__skip_uint64_val) $fields++;
        if (!$this->__skip_float_val) $fields++;
        if (!$this->__skip_double_val) $fields++;
        if (!$this->__skip_str_val) $fields++;
        if (!$this->__skip_vec_val) $fields++;
        if (!$this->__skip_dict_val) $fields++;
        return $fields;
    }
    public function rb_size()
    {
        $fields = 0;
        $size = 0;
        if (!$this->__skip_bool_val)
        {
            $size += $this->bool_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_int8_val)
        {
            $size += $this->int8_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_uint8_val)
        {
            $size += $this->uint8_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_int16_val)
        {
            $size += $this->int16_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_uint16_val)
        {
            $size += $this->uint16_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_int32_val)
        {
            $size += $this->int32_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_uint32_val)
        {
            $size += $this->uint32_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_int64_val)
        {
            $size += $this->int64_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_uint64_val)
        {
            $size += $this->uint64_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_float_val)
        {
            $size += $this->float_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_double_val)
        {
            $size += $this->double_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_str_val)
        {
            $size += $this->str_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_vec_val)
        {
            $size += $this->vec_val->rb_size();
            $fields++;
        }
        if (!$this->__skip_dict_val)
        {
            $size += $this->dict_val->rb_size();
            $fields++;
        }
        $size += rb_seek_field_table_item($fields);
        $size += rb_scalar_t::rb_size(rb_buf_end_t);
        return $size;
    }
    public function rb_encode($rb_val)
    {
        return rb_encode_base($this, $rb_val);
    }
    public function rb_decode($rb_val, $offset)
    {
        return rb_decode_base($rb_val, $offset, $this);
    }
    public function rb_dump($path)
    {
        return rb_dump_base($this, $path);
    }
    public function rb_load($path)
    {
        return rb_load_base($path, $this);
    }
}

?>
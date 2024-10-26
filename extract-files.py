#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixup_remove_arch_suffix,
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_clang_rt_ubsan,
    libs_proto_3_9_1,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
namespace_imports = [
    "hardware/qcom-caf/sm8150",
    "hardware/qcom-caf/wlan",
    "hardware/xiaomi",
    "vendor/qcom/opensource/commonsys/display",
    "vendor/qcom/opensource/commonsys-intf/display",
    "vendor/qcom/opensource/dataservices",
    "vendor/qcom/opensource/data-ipa-cfg-mgr-legacy-um",
    "vendor/qcom/opensource/display",
]
def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None
lib_fixups: lib_fixups_user_type = {
    libs_clang_rt_ubsan: lib_fixup_remove_arch_suffix,
    libs_proto_3_9_1: lib_fixup_vendorcompat,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.hardware.camera.device@3.2',
        'libmmosal',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'camera.device@1.0-impl.so',
        'camera.device@3.2-impl.so',
        'camera.device@3.3-impl.so',
        'camera.device@3.4-impl.so',
        'camera.device@3.5-impl.so',
    ): lib_fixup_vendor_suffix,
    (
        'libOmxCore',
        'libgrallocutils',
        'libwfdaac_vendor',
        'libhidlbase-v32',
        'libwpa_client',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/lib-imsvideocodec.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'vendor/lib/miwatermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    ('vendor/bin/sensors.qti', 'vendor/lib64/libsensorcal.so'): blob_fixup()
        .replace_needed('libprotobuf-cpp-lite-3.9.1.so', 'libprotobuf-cpp-full-3.9.1.so'),
    ('vendor/lib64/libwvhidl.so', 'vendor/lib64/mediadrm/libwvdrmengine.so', 'vendor/lib/mediadrm/libwvdrmengine.so'): blob_fixup()
        .replace_needed('libprotobuf-cpp-lite-3.9.1.so', 'libprotobuf-cpp-full-3.9.1.so')
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/libvendor.goodix.hardware.biometrics.fingerprint@2.1.so': blob_fixup()
        .remove_needed('libhidlbase.so')
        .replace_needed('libhidltransport.so', 'libhidlbase-v32.so'),
    'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
    'vendor/lib/hw/audio.primary.laurel_sprout.so': blob_fixup()
        .binary_regex_replace(b"vendor/lib/liba2dpoffload.so", b"liba2dpoffload_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libbatterylistener.so", b"libbatterylistener_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libcirrusspkrprot.so", b"libcirrusspkrprot_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libcomprcapture.so", b"libcomprcapture_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libexthwplugin.so", b"libexthwplugin_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libhdmiedid.so", b"libhdmiedid_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libhfp.so", b"libhfp_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libsndmonitor.so", b"libsndmonitor_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libspkrprot.so", b"libspkrprot_laurel_sprout.so")
        .binary_regex_replace(b"vendor/lib/libssrec.so", b"libssrec_laurel_sprout.so")

}  # fmt: skip

module = ExtractUtilsModule(
    'laurel_sprout',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)
if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

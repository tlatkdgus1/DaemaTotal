from . import upx

packing = []
def check_packing():
    upx_packing = upx.upx_unpack()

    packing.append(upx_packing)
    return packing


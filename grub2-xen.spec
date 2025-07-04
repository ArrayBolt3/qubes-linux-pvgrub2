# This package calls binutils components directly and would need to pass
# in flags to enable the LTO plugins
# Disable LTO
%global _lto_cflags %{nil}

# Prevents fails-to-build-from-source.
%undefine _hardened_build

# Modules always contain just 32-bit code
%define _libdir %{_exec_prefix}/lib

%global tarversion 2.12
%undefine _missing_build_ids_terminate_build

%global _configure ../configure

%undefine _package_note_file

Name:           grub2-xen
Version:        2.12
Release:        3%{?dist}
Summary:        Bootloader with support for Linux, Multiboot and more, for Xen PV

Group:          System Environment/Base
License:        GPLv3+
URL:            https://www.gnu.org/software/grub/
Source0:        https://ftp.gnu.org/gnu/grub/grub-%{tarversion}.tar.xz
Source1:        grub-bootstrap.cfg
Source2:        grub-xen.cfg
Source3:        extra_deps.lst

Patch0004: 0004-Rework-linux-command.patch
Patch0005: 0005-Rework-linux16-command.patch
Patch0007: 0007-IBM-client-architecture-CAS-reboot-support.patch
Patch0008: 0008-for-ppc-reset-console-display-attr-when-clear-screen.patch
Patch0009: 0009-Disable-GRUB-video-support-for-IBM-power-machines.patch
Patch0011: 0011-Allow-fallback-to-include-entries-by-title-not-just-.patch
Patch0012: 0012-Make-exit-take-a-return-code.patch
Patch0013: 0013-Make-efi-machines-load-an-env-block-from-a-variable.patch
Patch0014: 0014-Migrate-PPC-from-Yaboot-to-Grub2.patch
Patch0015: 0015-Add-fw_path-variable-revised.patch
Patch0016: 0016-Pass-x-hex-hex-straight-through-unmolested.patch
Patch0017: 0017-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch
Patch0018: 0018-Add-devicetree-loading.patch
Patch0019: 0019-Enable-pager-by-default.-985860.patch
Patch0020: 0020-Don-t-say-GNU-Linux-in-generated-menus.patch
Patch0021: 0021-Add-.eh_frame-to-list-of-relocations-stripped.patch
Patch0022: 0022-Don-t-require-a-password-to-boot-entries-generated-b.patch
Patch0023: 0023-use-fw_path-prefix-when-fallback-searching-for-grub-.patch
Patch0024: 0024-Try-mac-guid-etc-before-grub.cfg-on-tftp-config-file.patch
Patch0025: 0025-Generate-OS-and-CLASS-in-10_linux-from-etc-os-releas.patch
Patch0026: 0026-Try-prefix-if-fw_path-doesn-t-work.patch
Patch0027: 0027-Make-grub2-mkconfig-construct-titles-that-look-like-.patch
Patch0028: 0028-Add-friendly-grub2-password-config-tool-985962.patch
Patch0029: 0029-tcp-add-window-scaling-support.patch
Patch0030: 0030-efinet-and-bootp-add-support-for-dhcpv6.patch
Patch0031: 0031-bootp-New-net_bootp6-command.patch
Patch0032: 0032-Add-grub-get-kernel-settings-and-use-it-in-10_linux.patch
Patch0033: 0033-Make-grub_fatal-also-backtrace.patch
Patch0035: 0035-macos-just-build-chainloader-entries-don-t-try-any-x.patch
Patch0036: 0036-grub2-btrfs-Add-ability-to-boot-from-subvolumes.patch
Patch0037: 0037-btrfs-fix-a-bad-null-check.patch
Patch0038: 0038-export-btrfs_subvol-and-btrfs_subvolid.patch
Patch0039: 0039-grub2-btrfs-03-follow_default.patch
Patch0040: 0040-grub2-btrfs-04-grub2-install.patch
Patch0041: 0041-grub2-btrfs-05-grub2-mkconfig.patch
Patch0042: 0042-grub2-btrfs-06-subvol-mount.patch
Patch0043: 0043-Fallback-to-old-subvol-name-scheme-to-support-old-sn.patch
Patch0044: 0044-Grub-not-working-correctly-with-btrfs-snapshots-bsc-.patch
Patch0045: 0045-Add-grub_efi_allocate_pool-and-grub_efi_free_pool-wr.patch
Patch0046: 0046-Use-grub_efi_.-memory-helpers-where-reasonable.patch
Patch0047: 0047-Add-PRIxGRUB_EFI_STATUS-and-use-it.patch
Patch0048: 0048-don-t-use-int-for-efi-status.patch
Patch0049: 0049-make-GRUB_MOD_INIT-declare-its-function-prototypes.patch
Patch0050: 0050-Don-t-guess-boot-efi-as-HFS-on-ppc-machines-in-grub-.patch
Patch0051: 0051-20_linux_xen-load-xen-or-multiboot-2-modules-as-need.patch
Patch0052: 0052-align-struct-efi_variable-better.patch
Patch0053: 0053-Add-BLS-support-to-grub-mkconfig.patch
Patch0054: 0054-Don-t-attempt-to-backtrace-on-grub_abort-for-grub-em.patch
Patch0055: 0055-Add-grub2-switch-to-blscfg.patch
Patch0056: 0056-normal-don-t-draw-our-startup-message-if-debug-is-se.patch
Patch0057: 0057-Work-around-some-minor-include-path-weirdnesses.patch
Patch0058: 0058-Make-it-possible-to-enabled-build-id-sha1.patch
Patch0059: 0059-make-better-backtraces.patch
Patch0060: 0060-Fixup-for-newer-compiler.patch
Patch0061: 0061-Don-t-attempt-to-export-the-start-and-_start-symbols.patch
Patch0062: 0062-Fixup-for-newer-compiler.patch
Patch0063: 0063-Add-support-for-non-Ethernet-network-cards.patch
Patch0064: 0064-efinet-UEFI-IPv6-PXE-support.patch
Patch0065: 0065-grub.texi-Add-net_bootp6-doument.patch
Patch0066: 0066-bootp-Add-processing-DHCPACK-packet-from-HTTP-Boot.patch
Patch0067: 0067-Fix-const-char-pointers-in-grub-core-net-bootp.c.patch
Patch0068: 0068-efinet-Setting-network-from-UEFI-device-path.patch
Patch0069: 0069-efinet-Setting-DNS-server-from-UEFI-protocol.patch
Patch0070: 0070-Support-UEFI-networking-protocols.patch
Patch0071: 0071-AUDIT-0-http-boot-tracker-bug.patch
Patch0072: 0072-grub-editenv-Add-incr-command-to-increment-integer-v.patch
Patch0073: 0073-Add-auto-hide-menu-support.patch
Patch0074: 0074-Add-grub-set-bootflag-utility.patch
Patch0075: 0075-docs-Add-grub-boot-indeterminate.service-example.patch
Patch0076: 0076-gentpl-add-disable-support.patch
Patch0077: 0077-gentpl-add-pc-firmware-type.patch
Patch0078: 0078-efinet-also-use-the-firmware-acceleration-for-http.patch
Patch0079: 0079-efi-http-Make-root_url-reflect-the-protocol-hostname.patch
Patch0080: 0080-Make-it-so-we-can-tell-configure-which-cflags-utils-.patch
Patch0081: 0081-Rework-how-the-fdt-command-builds.patch
Patch0082: 0082-Disable-non-wordsize-allocations-on-arm.patch
Patch0083: 0083-Prepend-prefix-when-HTTP-path-is-relative.patch
Patch0084: 0084-Make-grub_error-more-verbose.patch
Patch0085: 0085-Make-reset-an-alias-for-the-reboot-command.patch
Patch0086: 0086-Add-a-version-command.patch
Patch0087: 0087-Add-more-dprintf-and-nerf-dprintf-in-script.c.patch
Patch0088: 0088-Attempt-to-fix-up-all-the-places-Wsign-compare-error.patch
Patch0089: 0089-Don-t-use-Wno-sign-compare-Wno-conversion-Wno-error-.patch
Patch0090: 0090-Fix-getroot.c-s-trampolines.patch
Patch0091: 0091-Do-not-allow-stack-trampolines-anywhere.patch
Patch0092: 0092-Reimplement-boot_counter.patch
Patch0093: 0093-Fix-menu-entry-selection-based-on-ID-and-title.patch
Patch0094: 0094-Make-the-menu-entry-users-option-argument-to-be-opti.patch
Patch0095: 0095-Add-efi-export-env-and-efi-load-env-commands.patch
Patch0096: 0096-Export-all-variables-from-the-initial-context-when-c.patch
Patch0097: 0097-grub.d-Split-out-boot-success-reset-from-menu-auto-h.patch
Patch0098: 0098-Don-t-assume-that-boot-commands-will-only-return-on-.patch
Patch0099: 0099-grub-set-bootflag-Update-comment-about-running-as-ro.patch
Patch0100: 0100-grub-set-bootflag-Write-new-env-to-tmpfile-and-then-.patch
Patch0101: 0101-grub.d-Fix-boot_indeterminate-getting-set-on-boot_su.patch
Patch0102: 0102-Add-start-symbol-for-RISC-V.patch
Patch0104: 0104-efi-http-Export-fw-http-_path-variables-to-make-them.patch
Patch0105: 0105-efi-http-Enclose-literal-IPv6-addresses-in-square-br.patch
Patch0106: 0106-efi-net-Allow-to-specify-a-port-number-in-addresses.patch
Patch0107: 0107-efi-ip4_config-Improve-check-to-detect-literal-IPv6-.patch
Patch0108: 0108-efi-net-Print-a-debug-message-if-parsing-the-address.patch
Patch0109: 0109-kern-term-Also-accept-F8-as-a-user-interrupt-key.patch
Patch0110: 0110-http-Prepend-prefix-when-the-HTTP-path-is-relative-a.patch
Patch0111: 0111-Fix-a-missing-return-in-efi-export-env-and-efi-load-.patch
Patch0112: 0112-efi-dhcp-fix-some-allocation-error-checking.patch
Patch0113: 0113-efi-http-fix-some-allocation-error-checking.patch
Patch0114: 0114-efi-ip-46-_config.c-fix-some-potential-allocation-ov.patch
Patch0115: 0115-Fix-const-char-pointers-in-grub-core-net-efi-ip4_con.patch
Patch0116: 0116-Fix-const-char-pointers-in-grub-core-net-efi-ip6_con.patch
Patch0117: 0117-Fix-const-char-pointers-in-grub-core-net-efi-net.c.patch
Patch0118: 0118-Fix-const-char-pointers-in-grub-core-net-efi-pxe.c.patch
Patch0121: 0121-at_keyboard-use-set-1-when-keyboard-is-in-Translate-.patch
Patch0123: 0123-New-with-debug-timestamps-configure-flag-to-prepend-.patch
Patch0124: 0124-Added-debug-statements-to-grub_disk_open-and-grub_di.patch
Patch0125: 0125-Introduce-function-grub_debug_is_enabled-void-return.patch
Patch0126: 0126-Don-t-clear-screen-when-debugging-is-enabled.patch
Patch0127: 0127-grub_file_-instrumentation-new-file-debug-tag.patch
Patch0128: 0128-ieee1275-Avoiding-many-unecessary-open-close.patch
Patch0129: 0129-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
Patch0130: 0130-ieee1275-powerpc-enables-device-mapper-discovery.patch
Patch0131: 0131-Add-at_keyboard_fallback_set-var-to-force-the-set-ma.patch
Patch0132: 0132-Add-suport-for-signing-grub-with-an-appended-signatu.patch
Patch0133: 0133-docs-grub-Document-signing-grub-under-UEFI.patch
Patch0134: 0134-docs-grub-Document-signing-grub-with-an-appended-sig.patch
Patch0135: 0135-dl-provide-a-fake-grub_dl_set_persistent-for-the-emu.patch
Patch0136: 0136-pgp-factor-out-rsa_pad.patch
Patch0137: 0137-crypto-move-storage-for-grub_crypto_pk_-to-crypto.c.patch
Patch0138: 0138-posix_wrap-tweaks-in-preparation-for-libtasn1.patch
Patch0139: 0139-libtasn1-import-libtasn1-4.16.0.patch
Patch0140: 0140-libtasn1-disable-code-not-needed-in-grub.patch
Patch0141: 0141-libtasn1-changes-for-grub-compatibility.patch
Patch0142: 0142-libtasn1-compile-into-asn1-module.patch
Patch0143: 0143-test_asn1-test-module-for-libtasn1.patch
Patch0144: 0144-grub-install-support-embedding-x509-certificates.patch
Patch0145: 0145-appended-signatures-import-GNUTLS-s-ASN.1-descriptio.patch
Patch0146: 0146-appended-signatures-parse-PKCS-7-signedData-and-X.50.patch
Patch0147: 0147-appended-signatures-support-verifying-appended-signa.patch
Patch0148: 0148-appended-signatures-verification-tests.patch
Patch0149: 0149-appended-signatures-documentation.patch
Patch0150: 0150-ieee1275-enter-lockdown-based-on-ibm-secure-boot.patch
Patch0151: 0151-ieee1275-drop-HEAP_MAX_ADDR-HEAP_MIN_SIZE.patch
Patch0152: 0152-appendedsig-x509-Also-handle-the-Extended-Key-Usage-.patch
Patch0153: 0153-ieee1275-ofdisk-retry-on-open-failure.patch
Patch0154: 0154-efinet-Add-DHCP-proxy-support.patch
Patch0155: 0155-Don-t-update-the-cmdline-when-generating-legacy-menu.patch
Patch0156: 0156-Suppress-gettext-error-message.patch
Patch0157: 0157-grub-set-password-Always-use-boot-grub2-user.cfg-as-.patch
Patch0158: 0158-normal-main-Discover-the-device-to-read-the-config-f.patch
Patch0159: 0159-powerpc-adjust-setting-of-prefix-for-signed-binary-c.patch
Patch0160: 0160-powerpc-ieee1275-load-grub-at-4MB-not-2MB.patch
Patch0161: 0161-Add-Fedora-location-of-DejaVu-SANS-font.patch
Patch0162: 0162-efi-new-connectefi-command.patch
Patch0163: 0163-powerpc-prefix-detection-support-device-names-with-c.patch
Patch0164: 0164-make-ofdisk_retries-optional.patch
Patch0165: 0165-misc-Make-grub_min-and-grub_max-more-resilient.patch
Patch0166: 0166-ReiserFS-switch-to-using-grub_min-grub_max.patch
Patch0167: 0167-misc-make-grub_boot_time-also-call-grub_dprintf-boot.patch
Patch0168: 0168-modules-make-.module_license-read-only.patch
Patch0169: 0169-modules-strip-.llvm_addrsig-sections-and-similar.patch
Patch0170: 0170-modules-Don-t-allocate-space-for-non-allocable-secti.patch
Patch0171: 0171-modules-load-module-sections-at-page-aligned-address.patch
Patch0172: 0172-nx-add-memory-attribute-get-set-API.patch
Patch0173: 0173-nx-set-page-permissions-for-loaded-modules.patch
Patch0174: 0174-nx-set-the-nx-compatible-flag-in-EFI-grub-images.patch
Patch0175: 0175-grub_fs_probe-dprint-errors-from-filesystems.patch
Patch0176: 0176-Make-debug-file-show-which-file-filters-get-run.patch
Patch0177: 0177-BLS-create-etc-kernel-cmdline-during-mkconfig.patch
Patch0178: 0178-squish-don-t-dup-rhgb-quiet-check-mtimes.patch
Patch0179: 0179-squish-give-up-on-rhgb-quiet.patch
Patch0180: 0180-squish-BLS-only-write-etc-kernel-cmdline-if-writable.patch
Patch0181: 0181-blscfg-Don-t-root-device-in-emu-builds.patch
Patch0182: 0182-ppc64le-signed-boot-media-changes.patch
Patch0183: 0183-core-Fix-several-implicit-function-declarations.patch
Patch0184: 0184-ieee1275-request-memory-with-ibm-client-architecture.patch
Patch0185: 0185-hostdisk-work-around-proc-not-reporting-size.patch
Patch0186: 0186-blscfg-check-for-mounted-boot-in-emu.patch
Patch0187: 0187-grub_dl_set_mem_attrs-fix-format-string.patch
Patch0188: 0188-grub_dl_set_mem_attrs-add-self-check-for-the-tramp-G.patch
Patch0189: 0189-grub_dl_load_segments-page-align-the-tramp-GOT-areas.patch
Patch0190: 0190-emu-Add-switch-root-to-grub-emu.patch
Patch0191: 0191-util-Enable-default-kernel-for-updates.patch
Patch0192: 0192-efi-http-change-uint32_t-to-uintn_t.patch
Patch0194: 0194-Fix-missing-include-in-ofdisk.c.patch
Patch0195: 0195-add-flag-to-only-search-root-dev.patch
Patch0196: 0196-cryptdisk-fix-incorrect-sign-comparison.patch
Patch0197: 0197-grub-install-fix-a-sign-comparison-error.patch
Patch0198: 0198-grub-mount-work-around-bad-integer-comparison.patch
Patch0199: 0199-power-Fix-use-after-free-in-get_slave_from_dm.patch
Patch0200: 0200-Fix-some-sign-comparison-errors.patch
Patch0201: 0201-normal-Fix-a-discarded-const.patch
Patch0202: 0202-at_keyboard-mark-grub_keyboard_controller_write-unus.patch
Patch0203: 0203-Fix-another-minor-sign-comparison-error.patch
Patch0204: 0204-Track-explicit-module-dependencies-in-Makefile.core..patch
Patch0205: 0205-Revert-mm-Assert-that-we-preserve-header-vs-region-a.patch
Patch0206: 0206-make-use-the-_CPU-variety-of-build-flags-for-PROGRAM.patch
Patch0207: 0207-Work-around-extra_deps.lst-issue.patch
Patch0208: 0208-include-proper-attribute-for-an-EFI-API-call-definit.patch
Patch0209: 0209-cast-grub_error-status-parameter.patch
Patch0210: 0210-remove-unused-varible.patch
Patch0211: 0211-cast-grub_net_bootp_packet-pointer.patch
Patch0212: 0212-libtasn1-fix-string-overflow-warning.patch
Patch0213: 0213-Add-support-for-Linux-EFI-stub-loading.patch
Patch0214: 0214-fix-i386_pc-on-legacycfg-module.patch
Patch0215: 0215-Add-secureboot-support-on-efi-chainloader.patch
Patch0216: 0216-Make-any-of-the-loaders-that-link-in-efi-mode-honor-.patch
Patch0217: 0217-Minimize-the-sort-ordering-for-.debug-and-rescue-ker.patch
Patch0218: 0218-Add-grub_qdprintf-grub_dprintf-without-the-file-line.patch
Patch0219: 0219-Make-a-gdb-dprintf-that-tells-us-load-addresses.patch
Patch0220: 0220-Handle-multi-arch-64-on-32-boot-in-linuxefi-loader.patch
Patch0221: 0221-Try-to-pick-better-locations-for-kernel-and-initrd.patch
Patch0222: 0222-x86-efi-Use-bounce-buffers-for-reading-to-addresses-.patch
Patch0223: 0223-x86-efi-Re-arrange-grub_cmd_linux-a-little-bit.patch
Patch0224: 0224-x86-efi-Make-our-own-allocator-for-kernel-stuff.patch
Patch0225: 0225-x86-efi-Allow-initrd-params-cmdline-allocations-abov.patch
Patch0226: 0226-efi-Set-image-base-address-before-jumping-to-the-PE-.patch
Patch0227: 0227-x86-efi-Reduce-maximum-bounce-buffer-size-to-16-MiB.patch
Patch0228: 0228-efilinux-Fix-integer-overflows-in-grub_cmd_initrd.patch
Patch0229: 0229-linuxefi-fail-kernel-validation-without-shim-protoco.patch
Patch0230: 0230-Allow-chainloading-EFI-apps-from-loop-mounts.patch
Patch0231: 0231-grub-core-loader-i386-efi-linux.c-do-not-validate-ke.patch
Patch0232: 0232-grub-core-loader-efi-chainloader.c-do-not-validate-c.patch
Patch0233: 0233-grub-core-loader-efi-linux.c-drop-now-unused-grub_li.patch
Patch0234: 0234-loader-efi-chainloader-grub_load_and_start_image-doe.patch
Patch0235: 0235-loader-efi-chainloader-simplify-the-loader-state.patch
Patch0236: 0236-loader-efi-chainloader-Use-grub_loader_set_ex.patch
Patch0237: 0237-loader-i386-efi-linux-Avoid-a-use-after-free-in-the-.patch
Patch0238: 0238-loader-i386-efi-linux-Use-grub_loader_set_ex.patch
Patch0239: 0239-loader-i386-efi-linux-Fix-a-memory-leak-in-the-initr.patch
Patch0240: 0240-EFI-allocate-kernel-in-EFI_RUNTIME_SERVICES_CODE-ins.patch
Patch0241: 0241-efi-use-enumerated-array-positions-for-our-allocatio.patch
Patch0242: 0242-efi-split-allocation-policy-for-kernel-vs-initrd-mem.patch
Patch0243: 0243-efi-allocate-the-initrd-within-the-bounds-expressed-.patch
Patch0244: 0244-efi-use-EFI_LOADER_-CODE-DATA-for-kernel-and-initrd-.patch
Patch0245: 0245-x86-efi-Fix-an-incorrect-array-size-in-kernel-alloca.patch
Patch0248: 0248-chainloader-remove-device-path-debug-message.patch
Patch0249: 0249-grub-set-bootflag-Conservative-partial-fix-for-CVE-2.patch
Patch0250: 0250-grub-set-bootflag-More-complete-fix-for-CVE-2024-104.patch
Patch0251: 0251-grub-set-bootflag-Exit-calmly-when-not-running-as-ro.patch
Patch0252: 0252-Makefile.core.def-fix-linux-module.patch
Patch0253: 0253-Add-support-for-Linux-EFI-stub-loading-on-arm-archit.patch
Patch0254: 0254-arm-arm64-loader-Better-memory-allocation-and-error-.patch
Patch0255: 0255-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch0256: 0256-pe-add-the-DOS-header-struct-and-fix-some-bad-naming.patch
Patch0257: 0257-Correct-BSS-zeroing-on-aarch64.patch
Patch0258: 0258-arm64-Use-proper-memory-type-for-kernel-allocation.patch
Patch0259: 0259-normal-Remove-grub_env_set-prefix-in-grub_try_normal.patch
Patch0260: 0260-fs-xfs-Handle-non-continuous-data-blocks-in-director.patch
Patch0261: 0261-Ignore-warnings-for-incompatible-types.patch
Patch0262: 0262-cmd-search-Rework-of-CVE-2023-4001-fix.patch
Patch0263: 0263-loader-efi-linux.c-read-the-kernel-image-before-head.patch
Patch0264: 0264-nx-set-attrs-in-our-kernel-loaders.patch
Patch0265: 0265-efi-Provide-wrappers-for-load_image-start_image.patch
Patch0266: 0266-efi-Disallow-fallback-to-legacy-Linux-loader-when-sh.patch
Patch0267: 0267-Set-non-executable-stack-sections-on-EFI-assembly-fi.patch
Patch0268: 0268-grub-mkconfig.in-turn-off-executable-owner-bit.patch
Patch0269: 0269-kern-ieee1275-init-Add-IEEE-1275-Radix-support-for-K.patch
Patch0270: 0270-grub2-mkconfig-Ensure-grub-cfg-stub-is-not-overwritt.patch
Patch0271: 0271-grub2-mkconfig-Simplify-os_name-detection.patch
Patch0272: 0272-grub-mkconfig-Remove-check-for-mount-point-for-grub-.patch
Patch0273: 0273-efi-api.h-include-missing-__grub_efi_api-macros-on-E.patch
Patch0274: 0274-grub-core-net-arp.c-fix-variable-name.patch
Patch0275: 0275-load-EFI-commands-inside-test-expressions.patch
Patch0276: 0276-efi-loader-Check-if-NX-is-required-in-grub_efi_linux.patch
Patch0277: 0277-Stop-grub.efi-from-always-printing-dynamic_load_symb.patch
Patch0278: 0278-acpi-Fix-out-of-bounds-access-in-grub_acpi_xsdt_find.patch
Patch0279: 0279-cmd-search-Fix-a-possible-NULL-ptr-dereference.patch
Patch0280: 0280-Enable-building-blscfg-module-on-xen-and-xen_pvh.patch
Patch0281: 0281-loader-efi-Fix-RISC-V-build.patch
Patch0282: 0282-kern-riscv-efi-init-Use-time-register-in-grub_efi_ge.patch
Patch0283: 0283-Use-medany-instead-of-large-model-for-RISCV.patch
Patch0284: 0284-fs-xfs-Fix-large-extent-counters-incompat-feature-su.patch
Patch0300: 0300-Add-Xen-parameter-parsing.patch


BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  dejavu-sans-fonts
BuildRequires:  device-mapper-devel
BuildRequires:  efi-srpm-macros
BuildRequires:  flex
BuildRequires:  freetype-devel
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  help2man
BuildRequires:  ncurses-devel
BuildRequires:  python3
BuildRequires:  rpm-devel
BuildRequires:  rpm-libs
BuildRequires:  squashfs-tools
BuildRequires:  texinfo
BuildRequires:	xen-devel
BuildRequires:  xz-devel

Requires:	gettext which file

ExcludeArch:	s390 s390x %{arm}

%description
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It support rich varietyof kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for PC BIOS systems.

%package pvh
Summary:	Bootloader with support for Linux, Multiboot and more, for Xen PVH
Group:		System Environment/Base
Requires:	gettext which file

%description pvh
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It support rich varietyof kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for Xen PVH.

%prep
%autosetup -p1 -n grub-%{tarversion}
cp %{SOURCE3} grub-core/
mkdir grub-xen-x86_64
cp %{SOURCE1} %{SOURCE2} grub-xen-x86_64/
mkdir grub-xen_pvh-i386
cp %{SOURCE1} %{SOURCE2} grub-xen_pvh-i386/

%build
LDFLAGS="$(echo $LDFLAGS | sed -e 's/-Wl,--build-id=sha1//g' )"
export LDFLAGS

./autogen.sh
cd grub-xen-x86_64
%configure							\
	CFLAGS="$(echo $RPM_OPT_FLAGS | sed			\
		-e 's/-O.//g'					\
		-e 's/-fstack-protector\(-[[:alnum:]]\+\)*//g'	\
		-e 's/-Wp,-D_FORTIFY_SOURCE=[[:digit:]]//g'	\
		-e 's/--param=ssp-buffer-size=4//g'		\
		-e 's/-mregparm=3/-mregparm=4/g'		\
		-e 's/-fexceptions//g'				\
		-e 's/-fcf-protection//g'			\
		-e 's/-fasynchronous-unwind-tables//g' )"	\
	TARGET_LDFLAGS=-static					\
	--with-platform=xen					\
	--with-grubdir=%{name}					\
	--program-transform-name=s,grub,%{name},		\
	--disable-grub-mount					\
	--disable-werror
make %{?_smp_mflags}
tar cf memdisk.tar grub-xen.cfg
./grub-mkimage -O x86_64-xen -o grub-x86_64-xen.bin \
		-c grub-bootstrap.cfg -m memdisk.tar -d grub-core grub-core/*.mod
cd ..
cd grub-xen_pvh-i386
%configure							\
	CFLAGS="$(echo $RPM_OPT_FLAGS | sed			\
		-e 's/-m64//g'					\
		-e 's/-O.//g'					\
		-e 's/-fstack-protector\(-[[:alnum:]]\+\)*//g'	\
		-e 's/-Wp,-D_FORTIFY_SOURCE=[[:digit:]]//g'	\
		-e 's/--param=ssp-buffer-size=4//g'		\
		-e 's/-mregparm=3/-mregparm=4/g'		\
		-e 's/-fexceptions//g'				\
		-e 's/-fcf-protection//g'			\
		-e 's/-fasynchronous-unwind-tables//g' )"	\
	TARGET_LDFLAGS=-static					\
    --target=i386-redhat-linux-gnu				\
	--with-platform=xen_pvh	    				\
	--with-grubdir=%{name}-pvh				\
	--program-transform-name=s,grub,%{name}-pvh,		\
	--disable-grub-mount					\
	--disable-werror
make %{?_smp_mflags}
tar cf memdisk.tar grub-xen.cfg
./grub-mkimage -O i386-xen_pvh -o grub-i386-xen_pvh.bin \
		-c grub-bootstrap.cfg -m memdisk.tar -d grub-core grub-core/*.mod
cd ..

%install
set -e
rm -fr $RPM_BUILD_ROOT

for dir in grub-xen-x86_64 grub-xen_pvh-i386; do
    make -C $dir DESTDIR=$RPM_BUILD_ROOT install
done
find $RPM_BUILD_ROOT -iname "*.module" -exec chmod a-x {} \;

install -d $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2
install -m 0644 grub-xen-x86_64/grub-x86_64-xen.bin $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2/
ln -s grub-x86_64-xen.bin $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2/vmlinuz
# "empty" file file so Qubes tools does not complain
echo -n | gzip > $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2/initramfs

install -d $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2-pvh
install -m 0644 grub-xen_pvh-i386/grub-i386-xen_pvh.bin $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2-pvh/
ln -s grub-i386-xen_pvh.bin $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2-pvh/vmlinuz
# "empty" file file so Qubes tools does not complain
echo -n | gzip > $RPM_BUILD_ROOT/var/lib/qubes/vm-kernels/pvgrub2-pvh/initramfs

# Install ELF files modules and images were created from into
# the shadow root, where debuginfo generator will grab them from
find $RPM_BUILD_ROOT -name '*.mod' -o -name '*.img' |
while read MODULE
do
        BASE=$(echo $MODULE |sed -r "s,.*/([^/]*)\.(mod|img),\1,")
        # Symbols from .img files are in .exec files, while .mod
        # modules store symbols in .elf. This is just because we
        # have both boot.img and boot.mod ...
        EXT=$(echo $MODULE |grep -q '.mod' && echo '.elf' || echo '.exec')
        TGT=$(echo $MODULE |sed "s,$RPM_BUILD_ROOT,.debugroot,")
#        install -m 755 -D $BASE$EXT $TGT
done

rm -r $RPM_BUILD_ROOT%{_sysconfdir}
rm -r $RPM_BUILD_ROOT%{_datarootdir}/grub
rm -r $RPM_BUILD_ROOT%{_datarootdir}/locale
rm -r $RPM_BUILD_ROOT%{_infodir}

rm -r $RPM_BUILD_ROOT%{_bindir}
rm -r $RPM_BUILD_ROOT%{_sbindir}
rm -r $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/grub/*-xen/
/var/lib/qubes/vm-kernels/pvgrub2/grub-x86_64-xen.bin
/var/lib/qubes/vm-kernels/pvgrub2/vmlinuz
/var/lib/qubes/vm-kernels/pvgrub2/initramfs
%doc COPYING

%files pvh
%defattr(-,root,root,-)
%{_libdir}/grub/*-xen_pvh/
/var/lib/qubes/vm-kernels/pvgrub2-pvh/grub-i386-xen_pvh.bin
/var/lib/qubes/vm-kernels/pvgrub2-pvh/vmlinuz
/var/lib/qubes/vm-kernels/pvgrub2-pvh/initramfs
%doc COPYING

%changelog

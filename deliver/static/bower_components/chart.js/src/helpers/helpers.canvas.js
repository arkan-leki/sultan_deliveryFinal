S      �   R      @  z  �    &      �      >  �  �      �      �  Z    �   }      V  �   �   �   �      �  �      �  �  ~  R  �  	  �  6   D  ]  c  _  �      �  �   �  �      �  �       �                �         �           �      �  �      �      4  r      A  ?  �          H  �  "      ?           �  8        9  *  �             8  U   �          �      �  �              {  �      O  �      :  �   �   �  Y           �  !      �  �  G      2   �   �      �  �    �    �  r  �    �   �   �  ]     �  �      �         *   t     �  ;  n       �  w  �   �  �      *          ;  �      �  �  �  �  T       :          @  .  �      �    �  2    �  $      �  _  )  �     �  U          �  �              Q  ^  �  �  /        �          A   �  �  �   �  �      y          �  g  �  �  #        �  r      -              �  /    '  �  /  s  a  l   �   �  �   x  V  �  �  t      }      M             �  $      �   �  C   �          �      �  O   '  }     K                  �      L  ^  �  C  �   =  �    �   r   z  5  X      c  �          {       �                      c  �   �  9  �    m      �  H  i  �    �      �  b  �      �       6  z          A  �            S  �   �  v   |  �   �  l  x  P  �  �         �     �    h  5      m      m   �      e  >   �   �   K  M  R  �  {  �  �    �  �  �  =          o  �     p  _      V  %  H   0  �  P   �  9   J   �  +  �  .  �   �  �     <  �  �    R   �  �   �      F      <  g     �  j           \  �  o  )       L  �      K  �          �  �  &  �  �   �  1   s   �  �  Y  �        �  �  �  �  �       �  �  �       ^  I  �  b  ,  �  �  �  �  �              R        7         �  y  �      %  �                h  �  �          I  o      �  �  B       �    W  �  S  �      q       B  �   �    P  p        #    L  W  �  \   �  z      3   �  s  `                 3  �       �      �    �  #  Y  #  �      !      t  w    �       �  �  �       	%Q (@i #%i, mod time %IM)
 	<@f metadata>
 	Using %s
 	Using %s, %s
 	created on %s 	last modified on %s 	last mounted on %s 	last mounted on %s on %s 
	while converting subcluster bitmap 
	while trying to add journal to device %s 
	while trying to create journal 
	while trying to create journal file 
	while trying to open journal on %s
 

%s: UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY.
	(i.e., without -a or -p options)
 

WARNING!!!  The filesystem is mounted.   If you continue you ***WILL***
cause ***SEVERE*** filesystem damage.

 
  %u free %s, %u free inodes, %u directories%s 
  Inode table at  
  Reserved GDT blocks at  
%12u inode used (%2.2f%%, out of %u)
 
%12u inodes used (%2.2f%%, out of %u)
 
%12u regular file
 
%12u regular files
 
%s: ***** FILE SYSTEM WAS MODIFIED *****
 
%s: ********** WARNING: Filesystem still has errors **********

 
Bad extended option(s) specified: %s

Extended options are separated by commas, and may take an argument which
	is set off by an equals ('=') sign.

Valid extended options are:
	superblock=<superblock number>
	blocksize=<blocksize>
 
Bad journal options specified.

Journal options are separated by commas, and may take an argument which
	is set off by an equals ('=') sign.

Valid journal options are:
	size=<journal size in megabytes>
	device=<journal device>
	location=<journal location>

The journal size must be between 1024 and 10240000 filesystem blocks.

 
Clearing the sparse superblock flag not supported.
 
Could not find journal device matching %s
 
Could not write %d blocks in inode table starting at %llu: %s
 
Emergency help:
 -p                   Automatic repair (no questions)
 -n                   Make no changes to the filesystem
 -y                   Assume "yes" to all questions
 -c                   Check for bad blocks and add them to the badblock list
 -f                   Force checking even if filesystem is marked clean
 
Error while enabling multiple mount protection feature. 
Filesystem too small for a journal
 
If the @b is really bad, the @f can not be fixed.
 
Interrupt caught, cleaning up
 
Invalid non-numeric argument to -%c ("%s")

 
Journal size too big for filesystem.
 
Resizing bigalloc file systems has not been fully tested.  Proceed at
your own risk!  Use the force option if you want to go ahead anyway.

 
Running additional passes to resolve @bs claimed by more than one @i...
Pass 1B: Rescanning for @m @bs
 
Running e2image on a R/W mounted filesystem can result in an
inconsistent image which will not be useful for debugging purposes.
Use -f option if you really want to do that.
 
Setting the sparse superblock flag not supported
for filesystems with the meta_bg feature enabled.
 
Sparse superblock flag set.  %s 
The @S could not be read or does not describe a valid ext2/ext3/ext4
@f.  If the @v is valid and it really contains an ext2/ext3/ext4
@f (and not swap or ufs or something else), then the @S
is corrupt, and you might try running e2fsck with an alternate @S:
    e2fsck -b 8193 <@v>
 or
    e2fsck -b 32768 <@v>

 
The bad @b @i has probably been corrupted.  You probably
should stop now and run e2fsck -c to scan for bad blocks
in the @f.
 
The device apparently does not exist; did you specify it correctly?
 
The filesystem already has sparse superblocks.
 
The requested journal size is %d blocks; it must be
between 1024 and 10240000 blocks.  Aborting.
 
Warning: '^quota' option overrides '-Q'arguments.
 
Warning: RAID stripe-width %u not an even multiple of stride %u.

 
Warning: the bigalloc feature is still under development
See https://ext4.wiki.kernel.org/index.php/Bigalloc for more information

 
Warning: the fs_type %s is not defined in mke2fs.conf

 
Your mke2fs.conf file does not define the %s filesystem type.
              # of inodes with ind/dind/tind blocks: %u/%u/%u
              Extent depth histogram:         %s -I device image-file
        %s -k
        %s -ra  [  -cfnp  ] [ -o src_offset ] [ -O dest_offset ] src_fs [ dest_fs ]
        %s [-r|t] [-n num] [-s socketpath]
   %s superblock at    Block bitmap at    Free blocks:    Free inodes:   %s remaining at %.2f MB/s  (%u fast symbolic link)
  (%u fast symbolic links)
  (EXPECTED 0x%04x)  (check after next mount)  (check deferred; on battery)  (check in %ld mounts)  (y/n)  Done.
  Group descriptor at   contains a file system with errors  has been mounted %u times without being checked  has filesystem last checked time in the future  has gone %u days without being checked  primary superblock features different from backup  was not cleanly unmounted #	Num=%llu, Size=%llu, Cursor=%llu, Sorted=%llu
 # Extent dump:
 %12llu block used (%2.2f%%, out of %llu)
 %12llu blocks used (%2.2f%%, out of %llu)
 %12u bad block
 %12u bad blocks
 %12u block device file
 %12u block device files
 %12u character device file
 %12u character device files
 %12u directory
 %12u directories
 %12u fifo
 %12u fifos
 %12u file
 %12u files
 %12u large file
 %12u large files
 %12u link
 %12u links
 %12u non-contiguous directory (%0d.%d%%)
 %12u non-contiguous directories (%0d.%d%%)
 %12u non-contiguous file (%0d.%d%%)
 %12u non-contiguous files (%0d.%d%%)
 %12u socket
 %12u sockets
 %12u symbolic link %12u symbolic links %6.2f%% done, %s elapsed. (%d/%d/%d errors) %6lu(%c): expecting %6lu got phys %6lu (blkcnt %lld)
 %B (%b) causes @d to be too big.   %B (%b) causes file to be too big.   %B (%b) causes symlink to be too big.   %B (%b) overlaps @f metadata in @i %i.   %d blocks already contained the data to be copied
 %d-byte blocks too big for system (max %d) %llu / %llu blocks (%d%%) %llu blocks (%
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <alias for the key>" >&2
    exit 1
fi

KEYS_DIR=/usr/local/etc/ansible/my_keys/$1
SSH_VARS_DIR=/usr/local/etc/ansible/ssh_vars
mkdir -p $KEYS_DIR
mkdir -p $SSH_VARS_DIR
if [ ! -f $SSH_VARS_DIR/ssh_users.yml ]; then
    echo "---" >> $SSH_VARS_DIR/ssh_users.yml
    echo "ssh_users:" >> $SSH_VARS_DIR/ssh_users.yml
fi

ssh-keygen -t rsa -b 4096 -C $1 -f $KEYS_DIR/id_rsa
echo "  - user:  $USER" >> $SSH_VARS_DIR/ssh_users.yml
echo "    key:  \"{{ lookup('file','$KEYS_DIR/id_rsa.pub') }}\"" >> $SSH_VARS_DIR/ssh_users.yml

mkdir -p ~/.ssh
cp $KEYS_DIR/id_rsa* ~/.ssh

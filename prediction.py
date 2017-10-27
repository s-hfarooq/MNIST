import tensorflow as tf
from PIL import Image, ImageFilter


#saver = tf.train.Saver()

tf.reset_default_graph()
# Create some variables.

sess = tf.InteractiveSession()


#saver.restore(sess, "model.ckpt")
#print("W_conv1 : %s" % W_conv1.eval())


#saver = tf.train.import_meta_graph('savedModel.meta')


with tf.Session() as sess:
	new_saver = tf.train.import_meta_graph('savedModel-1000.meta')
	new_saver.restore(sess, tf.train.latest_checkpoint('./'))
	print(sess.run('W_conv1'))


print ('\n\n\n\nDone.\n\n\n\n')
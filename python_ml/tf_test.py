import tensorflow as tf


def main():
    mnist = tf.keras.datasets.fashion_mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    _, accuracy = model.evaluate(x_test, y_test)
    print('Accuracy: {}'.format(accuracy))


if __name__ == '__main__':
    from timeit import default_timer as timer
    start = timer()
    main()
    end = timer()
    print("Elapsed time: {}".format(end-start))

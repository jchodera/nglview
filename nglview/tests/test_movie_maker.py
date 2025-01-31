import os

from mock import MagicMock, patch

import nglview
import pytraj
from make_dummy_comm import *

# local


class FakeEvent:
    def is_set(self):
        return self._event_set


@patch('moviepy.editor.ImageSequenceClip')
def test_movie_maker(ImageSequenceClip):
    from nglview.contrib.movie import MovieMaker
    ImageSequenceClip.write_gif = MagicMock()
    ImageSequenceClip.write_videofile = MagicMock()
    traj = pytraj.datafiles.load_tz2()
    view = nglview.show_pytraj(traj)

    movie = MovieMaker(view,
                       in_memory=True,
                       download_folder='here',
                       render_params={'factor': 4},
                       moviepy_params={},
                       stop=2)
    movie.make()
    movie.make_old_impl()
